import logging
import threading
import cv2
import os
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Video
from django.conf import settings

# Get an instance of a logger
logger = logging.getLogger(__name__)

# return video list all
def video_list_api(request):
    videos = Video.objects.values('id', 'file_path')
    video_list = list(videos)

    controller = CameraController()
    is_running = controller.is_recording
    camera_status = 'Camera is already running' if is_running else 'Camera is not running'

    return JsonResponse({'videos': video_list, 'isRunning': is_running, 'status':camera_status}, safe=False)

# return video(receive video_id)
def video_detail_api(request, video_id):
    try:
        video = Video.objects.get(id=video_id)
        return JsonResponse({'filePath': video.file_path})
    except Video.DoesNotExist:
        return JsonResponse({'error': 'Video Not Found'}, status=404)

# save video path to sqlite
def save_video_path(video_path):
    logger.debug("Video Save is Started!")
    video_name = os.path.basename(video_path)
    logger.debug(f"Video is Saved: {video_name}")
    Video.objects.create(file_path=video_name)

# manage camera
# this is singleton class
class CameraController:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # access lock -> only one person access this once.
        with cls._lock:
            # instance is not created still, create instance.
            if cls._instance is None:
                cls._instance = super(CameraController, cls).__new__(cls)
        # instance already created, return that.
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self._is_recording = False
            self._video_name = None

    @property
    def is_recording(self):
        return self._is_recording

    @is_recording.setter
    def is_recording(self, value):
        self._is_recording = value

    # start record
    def start_recording(self, video_name):
        video_path = os.path.join(settings.MEDIA_ROOT, video_name)  # 完全なパスを生成

        if not self._is_recording:
            try:
                self._is_recording = True
                self._video_name = video_path
                
                self._camera = cv2.VideoCapture(0)

                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                fps = 20.0
                frame_width = 640
                frame_height = 480
                
                self._video = cv2.VideoWriter(video_path, fourcc, fps, (frame_width, frame_height))

                threading.Thread(target=self._record_video).start()
            except Exception as e:
                logger.error(f"Failed to start recording: {e}", exc_info=True)
                self._is_recording = False

    # stop record
    def stop_recording(self):
        logger.debug("Stop Record Started!")
        if self._is_recording:
            try:
                self._is_recording = False
                if self._video:
                    logger.debug("Video Release Started!")
                    self._video.release()
                    logger.debug("Video Release is Completed!")
                save_video_path(self._video_name)
                logger.debug("Video Save is Completed!")
            except Exception as e:
                logger.error(f"Failed to stop recording: {e}", exc_info=True)

    # record video
    def _record_video(self):
        try:
            while self._is_recording:
                ret, frame = self._camera.read()
                if ret:
                    self._video.write(frame)
            self._video.release()
        except Exception as e:
            logger.error(f"Error during recording: {e}", exc_info=True)
            self._is_recording = False  # Ensure recording flag is set to False

# カメラ開始API
@require_POST
@csrf_exempt
def start_camera(request):
    logger.debug("Start Request Got!")
    # make controller for start record
    controller = CameraController()

    # recording status. default -> false
    if not controller.is_recording:
        logger.debug("Start Recoarding!")
        video_name = f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.mp4'
        controller.start_recording(video_name)
        return JsonResponse({'isRunning': True , 'status': 'Camera started'}, status=200)
    else:
        logger.debug("Already Start...")
        return JsonResponse({'isRunning': True, 'status': 'Camera is already running'}, status=200)

# カメラ停止API
@require_POST
@csrf_exempt
def stop_camera(request):
    logger.debug("Stop Request Got!")
    controller = CameraController()
    if controller.is_recording:
        controller.stop_recording()
        return JsonResponse({'isRunning': False, 'status': 'Camera stopped'}, status=200)
    else:
        return JsonResponse({'isRunning': False, 'status': 'Camera is not running'}, status=200)
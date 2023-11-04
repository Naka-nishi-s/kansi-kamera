import threading
import cv2
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import datetime
from  django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Top page
@login_required
def index_view(request):
    return render(request, 'index.html')

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
                cls._is_recording = False
                cls._camera = cv2.VideoCapture(0)
        # instance already created, return that.
        return cls._instance

    @property
    def is_recording(self):
        return self._is_recording

    @is_recording.setter
    def is_recording(self, value):
        self._is_recording = value

    # start record
    def start_recording(self, video_name):
        if not self._is_recording:
            # record starting & recording flag On
            self._is_recording = True
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            fps = 20.0
            frame_width = int(self._camera.get(3))
            frame_height = int(self._camera.get(4))
            self._video = cv2.VideoWriter(video_name, fourcc, fps, (frame_width, frame_height))

            # create new thread. thanks to this, catch other request.
            threading.Thread(target=self._record_video).start()

    # stop record
    def stop_recording(self):
        if self._is_recording:
            self._is_recording = False

    # record video
    def _record_video(self):
        while self._is_recording:
            ret, frame = self._camera.read()
            if ret:
                self._video.write(frame)
        self._video.release()

# カメラ開始API
@require_POST
@csrf_exempt
def start_camera(request):
    # make controller for start record
    controller = CameraController()

    # recording status. default -> false
    if not controller.is_recording:
        video_name = f'videos/{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.avi'
        controller.start_recording(video_name)
        return JsonResponse({'status': 'Camera started'}, status=200)
    else:
        return JsonResponse({'status': 'Camera is already running'}, status=200)

# カメラ停止API
@require_POST
@csrf_exempt
def stop_camera(request):
    controller = CameraController()
    if controller.is_recording:
        controller.stop_recording()
        return JsonResponse({'status': 'Camera stopped'}, status=200)
    else:
        return JsonResponse({'status': 'Camera is not running'}, status=200)
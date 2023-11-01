from django.shortcuts import render
from django.http import HttpResponse
import cv2
from .models import Video
import datetime

def watch_room(request):

    # get class for capture video
    capture = cv2.VideoCapture(0)

    # get frame size for video
    # 3 => frame width
    frame_width = int(capture.get(3))

    # 4 => frame height
    frame_height = int(capture.get(4))

    # create video writer Object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 20.0

    # save movie to unique name
    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    video_name = f'videos/{current_time}.avi'
    video = cv2.VideoWriter(video_name, fourcc, fps, (frame_width, frame_height))

    # continue get 1 frame image => video
    while True:
        # read variable from VideoCapture()
        ret, frame = capture.read()

        # success get frame => set 'ret' in 'true'
        # not success get frame => set 'ret' in 'false'
        if not ret:
            break

        # write in video
        video.write(frame)

        # show image
        cv2.imshow('Camera Stream', frame)

        # if pushed 'q' key, break loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # release area
    capture.release()
    video.release()
    cv2.destroyAllWindows()

    video_entry = Video(file_path=video_name)
    video_entry.save()

    return HttpResponse("Camera is Finished.")
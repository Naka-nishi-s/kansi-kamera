import cv2

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
video_name = 'output.avi'
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
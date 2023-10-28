import cv2

# get class for capture video
capture = cv2.VideoCapture(0)

# get frame size for video
# 3 => frame width
frame_width = int(capture.get(3))

# 4 => frame height
frame_height = int(capture.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))


# continue get 1 frame image => video
while True:
    # read variable from VideoCapture()
    ret, frame = capture.read()

    # success get frame => set 'ret' in 'true'
    # not success get frame => set 'ret' in 'false'
    if not ret:
        break

    video.write(frame)

    cv2.imshow('Camera Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
video.release()
cv2.destroyAllWindows()
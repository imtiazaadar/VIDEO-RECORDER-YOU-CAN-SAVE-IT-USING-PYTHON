import cv2
# Author : Imtiaz Adar
# Project : Video Capture
# Language : Python
def video_capture():
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        print('Sorry there is some error while opening the front camera')
    screen_height = capture.get(4)
    screen_width = capture.get(3)
    screen_size = (int(screen_width), int(screen_height))
    result = cv2.VideoWriter(f'{input("File name : ")}.avi', cv2.VideoWriter_fourcc(*'MJPG'), 25, screen_size)
    isCapturing = True
    while isCapturing:
        ret, video_frame = capture.read()
        if ret == True:
            result.write(video_frame)
            cv2.imshow("Imtiaz Adar's Camera", video_frame)
            if cv2.waitKey(10) == ord('q'):
                isCapturing = False
    capture.release()
    result.release()
    cv2.destroyAllWindows()

video_capture()
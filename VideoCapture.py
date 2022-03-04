import cv2
# Author : Imtiaz Adar
# Project : Video Capture
# Language : Python
capture = cv2.VideoCapture(0)
def record():
    global capture
    screen_height = capture.get(4)
    screen_width = capture.get(3)
    screen_size = (int(screen_width), int(screen_height))
    result = cv2.VideoWriter(f'{input("File name : ")}.avi', cv2.VideoWriter_fourcc(*'MJPG'), 25, screen_size)
    return result

def video_capture():
    global capture
    if not capture.isOpened():
        print('Sorry there is some error while opening the front camera')
    want_to_record = input('Do You Want To Record ?\nY/ Yes\nN/ No\n').lower()
    result = record()
    isCapturing = True
    while isCapturing:
        ret, video_frame = capture.read()
        if ret == True:
            if want_to_record == 'y':
                result.write(video_frame)
            cv2.imshow("Imtiaz Adar's Camera", video_frame)
            if cv2.waitKey(10) == ord('q'):
                isCapturing = False
    cv2.destroyAllWindows()

video_capture()
import cv2, winsound, time
# Author : Imtiaz Adar
# Project : Video Capture With Focus
# Language : Python

capture_video = cv2.VideoCapture(0)
def record():
    global capture_video
    screen_width = capture_video.get(3)
    screen_height = capture_video.get(4)
    screen_size = (int(screen_width), int(screen_height))
    result = cv2.VideoWriter(f'{input("File Name : ")}.avi', cv2.VideoWriter_fourcc(*'MJPG'), 25, screen_size)
    return result

def video_capture():
    global capture_video
    if not capture_video.isOpened():
        print('Sorry there is something wrong while opening the camera...')
    isCapturing = True
    minimum_threshold, maximum_threshold = 20, 255
    want_to_record = input('Do You Want To Record ?\nY/ Yes\nN/ No\n').lower()
    result = record()
    while isCapturing:
        _, video_frame1 = capture_video.read()
        _, video_frame2 = capture_video.read()
        absolute_difference = cv2.absdiff(video_frame1, video_frame2)
        gray_color = cv2.cvtColor(absolute_difference, cv2.COLOR_RGB2GRAY)
        lit_blur = cv2.GaussianBlur(gray_color, (5, 5), 0)
        _, thresh = cv2.threshold(lit_blur, minimum_threshold, maximum_threshold, cv2.THRESH_BINARY)
        dilate = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(video_frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if want_to_record == 'y':
            result.write(video_frame1)
        cv2.imshow("Imtiaz Adar's Camera", video_frame1)
        #winsound.PlaySound('Alarm.wav', winsound.SND_FILENAME)
        #time.sleep(1)
        if cv2.waitKey(10) == ord('q'):
            isCapturing = False
    cv2.destroyAllWindows()

video_capture()
#Import Libraries
import cv2
from cropImage import *

def camera():
    print("Hello camera")
    # capture from camera at location 0
    cap = cv2.VideoCapture(0)
    # set the width and height, and UNSUCCESSFULLY set the exposure time
    cap.set(3, 1280)
    cap.set(4, 1024)
    cap.set(15, 0.1)

    while True:
        ret, img = cap.read()
        frame = cv2.flip(img, 1)
        window_name = 'Image'
        center_coordinates = (680, 350)
        axesLength = (150, 200)
        angle = 0
        startAngle = 0
        endAngle = 360
        color = (55, 55, 255)
        thickness = 7
        image = cv2.ellipse(frame, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness)

        cv2.imshow('Image', image)
        if(cv2.waitKey(1) & 0xFF == ord('n')):
            return cap,crop(frame)
            break
        if (cv2.waitKey(2) & 0xFF == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()

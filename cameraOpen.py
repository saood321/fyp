#Import Libraries
import cv2
from cropImage import *

def camera():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('frame', frame)
        if(cv2.waitKey(1) & 0xFF == ord('n')):
            return crop(frame)
            break

    cap.release()
    cv2.destroyAllWindows()

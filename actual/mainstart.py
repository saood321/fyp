#import Libraries

from distanceCalculation import *
from cameraOpen import *
from landmarks import *
from cv2 import *
import sys

#functions
print("Hello main")
cap,face=camera()
if face==1:
    landmarks()
    distance()
    destroyWindow("Image")
    cap.release()


else:
    print("No Face Found")
    destroyWindow("Image")
    cap.release()









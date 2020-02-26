#import Libraries

from distanceCalculation import *
from cameraOpen import *
from landmarks import *


#functions
face=camera()
if face==1:
    landmarks()
    distance()
else:
    print("No Face Found")









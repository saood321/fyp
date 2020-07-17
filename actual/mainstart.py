
from distanceCalculation import *
from cameraOpen import *
from landmarks import *
from tkinter.messagebox import *


mood=camera()

res = isinstance(mood[0], str)
print(mood,str(res))
if (str(res)=="True"):
    print(mood[0])
    import MusicPlayer
    MusicPlayer.call(mood[0],"normal")


elif(mood==0):

    showerror("EBMP","no face found")












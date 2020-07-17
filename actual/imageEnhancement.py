import cv2
import matplotlib.pyplot as plt
from landmarks import *
def imageEnhance(img):

    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray_img_eqhist=cv2.equalizeHist(gray_img)
    return landmarks(gray_img_eqhist)


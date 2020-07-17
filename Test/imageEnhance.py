import cv2
import matplotlib.pyplot as plt
img= cv2.imread('image3.jpg')


cv2.imshow("1",img)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

hist=cv2.calcHist(gray_img,[0],None,[256],[0,256])

plt.subplot(121)
plt.title("Image1")
plt.xlabel('bins')
plt.ylabel("No of pixels")
plt.plot(hist)
plt.subplot(122)


gray_img_eqhist=cv2.equalizeHist(gray_img)
cv2.imshow("2",gray_img_eqhist)


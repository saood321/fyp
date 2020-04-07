import cv2

def resize(img):
    width = 350
    height = 350
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite('resizeface.jpg', resized)
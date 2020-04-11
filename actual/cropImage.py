import cv2
from resizeImage import *
def crop(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    print("Found {0} Faces.".format(len(faces)))
    if len(faces)>=1:

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = image[y:y + h, x:x + w]
            cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)
            img=str(w)+str(h)+'_faces.jpg'

        img = cv2.imread(img)
        cv2.imwrite('faces_detected.jpg', image)
        return resize(img)


    else:
        return 0





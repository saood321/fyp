#Import Libraries
import cv2
import dlib

def get_landmarks(resized):
    detector = dlib.get_frontal_face_detector()  # Face detector
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    img =resized

    xlist = ['T1']
    ylist = ['T2']

    detections = detector(img, 1)
    for k, d in enumerate(detections):  # For all detected face instances individually
        shape = predictor(img, d)  # Draw Facial Landmarks with the predictor class

        for i in range(1, 68):  # Store X and Y coordinates in two lists
            xlist.append(float(shape.part(i).x))
            ylist.append(float(shape.part(i).y))

    if len(detections) > 0:
        return xlist, ylist

    else:  # If no faces are detected, return error message to other function to handle
        landmarks = "error"
        return landmarks
        cap.release()
        cv2.destroyAllWindows()
        print("No face Detected")

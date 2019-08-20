import numpy as np
import cv2 as cv
import os
import random as rng
cap = cv.VideoCapture(os.getcwd()+'/Videos/Badminton1.mp4')

while cap.isOpened() :
    ret, frame = cap.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #_, thresh = cv.threshold(gray, 127, 255, 0)
        #th3 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
        x=200
        canny_output = cv.Canny(gray, x, x * 2)
        # contours, hierarchy = cv.findContours(th3, cv.)
        # Find contours
        contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        # Draw contours
        cv.drawContours(frame, contours, -1, (0, 255, 0), 3)
        #drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        #for i in range(len(contours)):
        #    color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        #    cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)

        cv.imshow('Original', frame)
        cv.imshow('Gray', gray)
        cv.imshow('Thresh', canny_output)
        #cv.imshow('Adaptive', th3)
        #cv.imshow('Canny', canny_output)
        # Show in a window
        #cv.imshow('Contours', drawing)

        key=cv.waitKey(0)
        if key == 27:
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
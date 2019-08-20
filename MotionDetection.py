import numpy as np
import cv2 as cv
import os
import random as rng
cap = cv.VideoCapture(os.getcwd()+'/Videos/Badminton1.mp4')
ret, frame1 = cap.read()
while cap.isOpened() :

    ret, frame2 = cap.read()

    if ret:
        frame = cv.absdiff(frame1, frame2)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (5,5), 0)

        _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
        dilated = cv.dilate(thresh, None, iterations=3)
        #th3 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
        #x=200
        #canny_output = cv.Canny(gray, x, x * 2)
        # contours, hierarchy = cv.findContours(th3, cv.)
        # Find contours
        contours, hierarchy = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # Draw contours
        cv.drawContours(frame1, contours, -1, (0, 255, 0), 3)
        #drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        #for i in range(len(contours)):
        #    color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        #    cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)

        cv.imshow('Diff', frame)
        cv.imshow('Origial', frame1)
        #cv.imshow('Thresh', canny_output)
        #cv.imshow('Adaptive', th3)
        #cv.imshow('Canny', canny_output)
        # Show in a window
        #cv.imshow('Contours', drawing)
        frame1 = frame2
        key=cv.waitKey(0)
        if key == 27:
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
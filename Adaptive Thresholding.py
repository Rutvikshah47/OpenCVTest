import cv2 as cv
import os
import numpy as np

img = cv.imread(os.getcwd()+'/Images/Shuttlecock1.jpg', 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)


cv.imshow("Sudoku", img)
cv.imshow("Th1", th1)
cv.imshow("Th2", th2)
cv.imshow("Th3", th3)

cv.waitKey(0)
cv.destroyAllWindows()
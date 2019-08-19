import cv2 as cv
import os
import numpy as np

img = cv.imread(os.getcwd()+'/Images/gradient.jpeg', 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# value is < 127 then it will 0 and > 127 it will 255 (White)

_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

# From 0 to 127 pixels remain same but > 127 will become 127

_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

# From 0 to 127 pixels will become 0 but > 127 will remain same

cv.imshow("Original", img)
cv.imshow("Th1", th1)
cv.imshow("Th2", th2)
cv.imshow("Th3", th3)
cv.imshow("Th4", th4)

cv.waitKey(0)
cv.destroyAllWindows()
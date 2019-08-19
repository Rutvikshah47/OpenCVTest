import cv2 as cv
import os

img = cv.imread(os.getcwd()+'/Images/lena.jpg', -1)

#print(img)


cv.imwrite(os.getcwd()+'/Images/Writed_Image_lena.jpg', img)

img = cv.imread(os.getcwd()+'/Images/Writed_Image_lena.jpg', 1)

cv.imshow('Display_Test', img)
#cv.waitKey(5000)
k = cv.waitKey(0)
if k == 27:  #if escape is press
    cv.destroyAllWindows()
elif k == ord('s'): #if s on keyboard press (s for save)
    cv.imwrite(os.getcwd() + '/Images/Writed_Image2_lena.jpg', img)
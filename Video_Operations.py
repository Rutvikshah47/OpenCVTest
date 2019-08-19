import cv2 as cv
import os

cap = cv.VideoCapture(os.getcwd()+'/Videos/testVideo.avi')


#fourcc = cv.VideoWriter_fourcc(*'XVID')
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(os.getcwd()+'/Videos/Writed_Video.avi', fourcc, 20.0, (100, 100))


# cap = cv.videoCapture(0)
print("Height of frame : ", cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print("Widht of frame : ", cap.get(cv.CAP_PROP_FRAME_WIDTH))
print("No of frames : ", cap.get(cv.CAP_PROP_FRAME_COUNT))
while( cap.isOpened() ) :
    ret, frame = cap.read()
    if ret == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        out.write(frame)

        cv.imshow('video_frame', gray)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()
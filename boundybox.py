import numpy as np
import cv2 as cv

#RESOURCES USED
#https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
#https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
#https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

cap = cv.VideoCapture(0)

while(1):

#code taken from 1 moments bounding box 
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    range_low = np.array([89, 150, 120])
    range_hi = np.array([160, 255, 255])
    mask = cv.inRange(hsv, range_low, range_hi)
    x,y,w,h = cv.boundingRect(mask)
    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow('frame', frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()

#My object was a pink notebook. When i shine a light on the pink notebook,
#the bounding box begins to prefer tracking my skin as opposed to the
#notebook!

#Higher brightness allows the color picker to work well!
import numpy as np
import cv2

camera = cv2.VideoCapture(0)

while True:
    ret,image =camera.read()
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100,60,60])
    upper_blue = np.array([140,255,255])
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    lastImage = cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow('Original Video',image)
    cv2.imshow('Mask Video',mask)
    cv2.imshow('Last Video',lastImage)

    if cv2.waitKey(25) and 0xFF==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
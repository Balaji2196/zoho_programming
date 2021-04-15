import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time

video_capture=cv2.VideoCapture(0)


while True:
    _,frame=video_capture.read()
    cv2.rectangle(frame,(200,200),(450,500),(0,0,255),2)
    imcrop=frame[202:498,202:448]
    blur=cv2.GaussianBlur(imcrop,(5,5),0)
    
    #imc=cv2.resize(imcrop,(256,256))
   
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lower_skin=np.array([0,40,30])
    upper_skin = np.array([43, 255, 254])
    mask=cv2.inRange(hsv,lower_skin,upper_skin)
    
    
    results=cv2.bitwise_and(imcrop,imcrop,mask=mask)

    mirror=cv2.flip(frame,1)
    #cv2.imshow("mask",mask)
    cv2.imshow("mirror",mirror)
    #cv2.imshow("video", frame)
    cv2.imshow("result",results)
    
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

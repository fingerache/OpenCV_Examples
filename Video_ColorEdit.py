#refer https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

import os
import cv2
import numpy as np
#import random


# hard-coded dependencies
os.chdir(r'C:\Users\310246616\Videos')


def imageShow(img, delay):
    cv2.imshow('test', img)
    cv2.waitKey(delay)
    if delay == 0:
        cv2.destroyAllWindows()

cap = cv2.VideoCapture('4ware.mp4')

i=0
while(cap.isOpened()):
     ret, frame = cap.read()
     if i == 0:
         x_mask = np.ones((1080, 1920, 3))
         x_mask[:50, 640:1280] = 0
     gray = frame[:,:,:]
     #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     mask = gray > 250
     val = 255 if (i % 24) > 8 and (i % 24 <= 16) else 127
     gray[mask] = val
     #gray = gray * x_mask
     imageShow(gray, 1)
     i = i+1

cv2.destroyAllWindows()

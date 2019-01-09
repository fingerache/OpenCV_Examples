import os
import cv2
import numpy as np
#import random


# hard-coded dependencies
os.chdir(r'C:\Users\310246616\Pictures')


def imageShow(img, delay):
    cv2.imshow('test', img)
    cv2.waitKey(delay)
    if delay == 0:
        cv2.destroyAllWindows()


def fader(img1, img2, steps):
    a = 0
    for i in range(steps):
        a = i/steps
        dst = cv2.addWeighted(img2, a, img1, 1-a, 0)
        imageShow(dst, 1)
    cv2.destroyAllWindows()


# hard-coded dependencies
img1 = cv2.imread("psychedelic_skull_wallpaper_Copy.jpg")

# copy image
img2 = img1[:,:,:]

# using masked array
marr1 = np.ma.array(img1, mask=img1 > 127, fill_value=0)
marr2 = np.ma.array(img1, mask=img1 <= 127, fill_value=0)

# changing values
marr1 = marr1*2/3
marr2 = 1-marr2/1

img2 = cv2.addWeighted(marr1.filled(), 0.5, marr2.filled(), 0.5, 0)
img2 = (img2 + 1)*255/2
img2 = np.uint8(img2)
imageShow(img1, 0)
cv2.destroyAllWindows()
imageShow(img2, 0)
cv2.destroyAllWindows()


fader(img2, img1, 6000)

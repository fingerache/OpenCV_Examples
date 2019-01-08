import os
import cv2
import numpy as np
#import random


# hard-coded dependencies
os.chdir(r'C:\Users\310246616\Pictures')

# hard-coded dependencies
img = cv2.imread("deadmau5.jpg")
print (img[100,100])

#ranged access
imgx = img[10:90, 10:90]

# create random image
random_img = np.random.random((1080, 1080, 3))

for i in range(30000):
    random_img = np.random.random((1080, 1080))
    cv2.imshow("test", random_img); cv2.waitKey(2)

times = 1080 / 20;

cv2.imshow("test", random_img); cv2.waitKey(10)

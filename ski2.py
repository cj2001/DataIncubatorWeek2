import numpy as np
import cv2
from matplotlib import pyplot as plt

im2 = cv2.imread('image_b2.tif',0)
im3 = cv2.imread('image_b3.tif',0)
im4 = cv2.imread('image_b4.tif',0)
im5 = cv2.imread('image_b5.tif',0)


base = np.ones(im2.shape)
im2n = im2 + base
im5n = im5 + base

num = np.absolute(im2n - im5n)
denom = im2n + im5n

ndsi = np.divide(num,denom)

tndsi = ndsi > 0.6

#tndsi = cv2.threshold(ndsi,alpha=0.4,beta=1.0,cv2.THRESH_BINARY)


plt.imshow(tndsi, cmap='gray')
plt.colorbar()
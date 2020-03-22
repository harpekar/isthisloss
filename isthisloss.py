#!/usr/bin/python

import cv2
from PIL import Image
import sys
import numpy as np
from matplotlib import pyplot as plt

#Prepare outline image
outline = cv2.imread('loss.jpg', cv2.IMREAD_GRAYSCALE)


#outline = cv2.cvtColor(outline, cv2.COLOR_BGR2GRAY) #grayscale outline image--make only one channel
#outline = cv2.Canny(outline, 100, 200)

img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE) #Read in user-provided image as a numpy array

if img.any() == None:
    raise Exception("Could not load image")

height, width = img.shape[:2] #Get image dimensions

th, im_th = cv2.threshold(outline, 125, 255,cv2.THRESH_BINARY_INV)

im_floodfill = im_th.copy()

h, w = im_th.shape[:2]

mask = np.zeros((h+2, w+2), np.uint8)

# Floodfill from point (0, 0)

cv2.floodFill(im_floodfill, mask, (0,0), 255);

# Invert floodfilled image

im_floodfill_inv = cv2.bitwise_not(im_floodfill)

# Combine the two images to get the foreground.

mask = im_th | im_floodfill_inv

# Display images.


    
cv2.imshow("Foreground", mask)

cv2.waitKey(0)

cv2.destroyAllWindows()

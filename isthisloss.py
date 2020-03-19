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

else:
    height, width = img.shape[:2] #Get image dimensions

    half_height = height/2
    half_width = width/2

    #to get more exact foreground/background detection, analyze each panel individually
    first_panel = img[0:half_height, 0:half_width]
    second_panel = img[0:half_height, half_width:width]
    third_panel = img[half_height:height, 0:half_width]
    fourth_panel = img[half_height:height, half_width:width] 

    cv2.imshow("Outline", first_panel)

    th, im_th = cv2.threshold(outline, 125, 255,cv2.THRESH_BINARY_INV)

    im_floodfill = im_th.copy()

    h, w = im_th.shape[:2]

    mask = np.zeros((h+2, w+2), np.uint8)

    # Floodfill from point (0, 0)

    cv2.floodFill(im_floodfill, mask, (0,0), 255);

    # Invert floodfilled image

    im_floodfill_inv = cv2.bitwise_not(im_floodfill)

    # Combine the two images to get the foreground.

    im_out = im_th | im_floodfill_inv

    # Display images.

    
    cv2.imshow("Foreground", im_out)

    cv2.waitKey(0)

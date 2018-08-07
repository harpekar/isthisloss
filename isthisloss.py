#!/usr/bin/python
import cv2
from PIL import Image
import sys
import numpy as np
from matplotlib import pyplot as plt

#Prepare outline image
outline = cv2.imread('loss-outline.jpg')
#outline = cv2.cvtColor(outline, cv2.COLOR_BGR2GRAY) #grayscale outline image--make only one channel
#outline = cv2.Canny(outline, 100, 200)

img = cv2.imread(sys.argv[1]) #Read in user-provided image

if img.any() == None:
    raise Exception("Could not load image")

else:
    graysc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale image
    #edges = cv2.Canny(graysc,100,200) #Finds edges in given image
    ret, thresh = cv2.threshold(graysc, 0,100,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    print (outline.shape)
    print (outline.size)
    print (outline.dtype)

#    print (edges.shape)
#    print (edges.size)
#    print (edges.dtype)

#    output = cv2.addWeighted(edges, 1, outline, 1, 0) #Overlays template from original image onto picture

    plt.imshow(thresh, cmap = 'gray')
    plt.show()

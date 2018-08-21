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

img = cv2.imread(sys.argv[1]) #Read in user-provided image as a numpy array

mask = np.zeros(img.shape[:2],np.uint8)

if img.any() == None:
    raise Exception("Could not load image")

else:
    height, width = img.shape[:2] #Get image dimensions
    firstPanel = img[0:height/2, 0:width/2]

    first_img = Image.fromarray(firstPanel, "RGB")
    
#plt.imshow(first_img)
#plt.show()

    graysc = cv2.cvtColor(firstPanel, cv2.COLOR_BGR2GRAY) #grayscale image
    #edges = cv2.Canny(graysc,100,200) #Finds edges in given image
    ret, thresh = cv2.threshold(graysc, 0,150,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    print (firstPanel.shape)
    print (firstPanel.size)
    print (firstPanel.dtype)

#    print (edges.shape)
#    print (edges.size)
#    print (edges.dtype)

#    output = cv2.addWeighted(edges, 1, outline, 1, 0) #Overlays template from original image onto picture

    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
     
#    plt.imshow(img),plt.colorbar(),plt.show()

    plt.imshow(thresh, cmap = 'gray')
    plt.show()

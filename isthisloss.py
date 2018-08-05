#!/usr/bin/python
import cv2
from PIL import Image
import sys
import numpy as np
from matplotlib import pyplot as plt

outline = cv2.imread('loss-outline.jpg')
img = cv2.imread(sys.argv[1])

if img.any() == None:
    raise Exception("Could not load image")

else:
    graysc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale image
    edges = cv2.Canny(graysc,100,200) #Finds edges in given image

    print (outline.shape)
    print (outline.size)
    print (outline.dtype)

    print (edges.shape)
    print (edges.size)
    print (edges.dtype)

    cv2.addWeighted(edges, 1, outline, 1, 0) #Overlays template from original image onto picture

    plt.imshow(edges, cmap = 'gray')
    plt.show()

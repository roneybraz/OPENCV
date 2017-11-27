# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:26:06 2017

@author: Aluno
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('FLOR.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    cv2 . imshow ( titles[i] , images[i] ) 
    cv2 . waitKey ( 0 ) 
    cv2 . destroyAllWindows ()

plt.show()
#cv2 . imshow ( 'Janela' , img ) 
#cv2 . waitKey ( 0 ) 
#cv2 . destroyAllWindows ()
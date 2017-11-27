# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:33:08 2017

@author: Aluno
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
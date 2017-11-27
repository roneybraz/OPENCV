# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:46:03 2017

@author: Aluno
"""

import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
#cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Kelry',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

#cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2 . imshow ( 'E o Cara' , img ) 
cv2 . waitKey ( 0 ) 
cv2 . destroyAllWindows ()

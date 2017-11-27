# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:12:30 2017

@author: Aluno
"""

import  cv2
# Carrega uma imagem colorida em grayscale 
img  =  cv2 . imread ( 'flor.jpg' )
b,g,r =cv2.split(img)
#cv2.imwrite('messigray.png',img)
#img[:,:,2]=0
cv2 . imshow ( 'OpenCV' ,g) 
cv2 . waitKey ( 0 ) 
cv2 . destroyAllWindows ()

#cv2.imwrite('messigray.png',img)

#cv2 . namedWindow ( 'imagem' ,  cv2 . WINDOW_NORMAL ) 


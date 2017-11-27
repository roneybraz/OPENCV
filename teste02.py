# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:30:39 2017

@author: Aluno
"""

import  numpy  as  np 
import  cv2 

img  =  cv2 . imread ( 'messi5.jpg' , 0 ) 
cv2 . imshow ( 'imagem' , img ) 
k = cv2.waitKey (0)# e 0xFF
if  k  ==  27 :          # aguarde a tecla ESC para sair do 
    cv2 . destroyAllWindows () 
elif  k  ==  ord ( 's' ):  # aguarde a tecla 's' para salvar e sair
    cv2 . imwrite ( 'messigray.png' , img ) 
    cv2 . destroyAllWindows ()
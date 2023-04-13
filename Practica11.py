# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 00:56:54 2022

@author: verom
"""
import cv2 as cv
import numpy as np
#OPERADOR DE ROBERTS


img = cv.imread ( 'unicornio.jpg' , cv.COLOR_BGR2GRAY ) 
rgb_img = cv.cvtColor ( img , cv.COLOR_BGR2RGB )

# Grayscale processing image 
grayImage = cv.cvtColor ( img , cv.COLOR_BGR2GRAY )

# Roberts operator 
kernelx = np.array ( [ [ -1,0 ] ,  [ 0 ,  1 ] ] , dtype = int ) 
kernely = np.array ( [ [ 0 ,  -1 ] ,  [ 1 , 0 ] ] , dtype = int )
    
x = cv . filter2D ( grayImage , cv.CV_16S , kernelx ) 
y = cv . filter2D ( grayImage , cv.CV_16S , kernely )

# Covertir imagen a unit8 
absX = cv.convertScaleAbs(x) 
absY = cv.convertScaleAbs(y) 
Roberts = cv.addWeighted ( absX ,  0.5 , absY ,  0.5 ,  0 )

cv.imshow("Unicornio.jpg",img)
cv.imwrite("Roberts.jpg",Roberts)
cv.imshow("Roberts.jpg",Roberts)



#Prewitt

# Prewitt operator 
kernelx = np.array ( [ [ 1 , 1 , 1 ] , [ 0 , 0 , 0 ] , [ -1 , - 1 , - 1 ] ] , dtype = int ) 
kernely = np.array ( [ [ -1 , 0 ,1 ] , [ -1 , 0 , 1 ] , [ -1 , 0 , 1 ] ] , dtype = int )

x = cv.filter2D ( grayImage , cv.CV_16S , kernelx ) 
y = cv.filter2D ( grayImage , cv.CV_16S , kernely )

# Turn uint8, image fusion 
absX = cv.convertScaleAbs (x) 
absY = cv.convertScaleAbs (y) 
Prewitt = cv.addWeighted ( absX ,  0.5 , absY ,  0.5 ,  0 )

cv.imwrite("Prewitt.jpg",Prewitt)
cv.imshow("Prewitt.jpg",Prewitt)


#Sobel
 
x = cv.Sobel (grayImage ,cv.CV_16S , 1 , 0 ) 
y = cv.Sobel ( grayImage , cv.CV_16S , 0 , 1 )

# Turn uint8, image fusion 
absX = cv.convertScaleAbs (x) 
absY = cv.convertScaleAbs (y) 
Sobel = cv.addWeighted ( absX ,  0.5 , absY ,  0.5 ,  0 )

cv.imwrite("Sobel.jpg",Sobel)
cv.imshow("Sobel.jpg",Sobel)


#Laplaciano

dst = cv.Laplacian( grayImage , cv.CV_16S ,ksize =  3 ) 
Laplacian = cv.convertScaleAbs ( dst )

cv.imwrite("Laplaciano.jpg",Laplacian)
cv.imshow("Laplaciano.jpg",Laplacian)
cv.waitKey(0)
cv.destroyAllWindows()

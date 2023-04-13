# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 23:00:53 2022

@author: verom
"""


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import copy
import math




# 1 lectura de imágenes
img = cv.imread('PerroSYP.jpg')
 # 2 filtrado de medios
blur = cv.blur(img,(5,5))
 # 3 visualización de imágenes
 
 
cv.imshow("PerroSYP.jpg",img)
cv.imwrite("PerroMedia.jpg",blur)
cv.imshow("PerroMedia.jpg",blur)


#FILTRO GAUSSIANO


img2 = cv.imread("PerroGauss.jpg")
Gauss = cv.GaussianBlur(img2,(3,3),1)
cv.imshow("PerroGauss.jpg",img2)
cv.imwrite("PerroGaussF.jpg",Gauss)
cv.imshow("PerroGaussF.jpg",Gauss)



#FILTRO MEDIANA



mediana = cv.medianBlur(img,5)
cv.imwrite("PerroMediana.jpg",mediana)
cv.imshow("PerroMediana.jpg",mediana)



#MAXIMO Y MINIMO
def spilt( a ):
    if a/2 == 0:
        x1 = x2 = a/2
    else:
        x1 = math.floor( a/2 )
        x2 = a - x1
    return -x1,x2

def original (i, j, k,a, b,im):
    x1, x2 = spilt(a)
    y1, y2 = spilt(b)
    temp = np.zeros(a * b)
    count = 0
    for m in range(x1, x2):
        for n in range(y1, y2):
            if i + m < 0 or i + m > im.shape[0] - 1 or j + n < 0 or j + n > im.shape[1] - 1:
                temp[count] = im[i, j, k]
            else:
                temp[count] = im[i + m, j + n, k]
            count += 1
    return  temp 

def max_functin(a, b, im):
    img = copy.copy(im)
    for i in range(0, im.shape[0]):
        for j in range(2, im.shape[1]):
            for k in range(im.shape[2]):
                temp = original(i, j, k, a, b, img)
                im[i, j, k] = np.max(temp)
    return im

def min_functin(a, b, im):
    img = copy.copy(im)
    for i in range(0, im.shape[0]):
        for j in range(2, im.shape[1]):
            for k in range(im.shape[2]):
                temp = original(i, j, k, a, b, img)
                im[i, j, k] = np.min(temp)
    return im

max_img = max_functin(3, 3, copy.copy(img))
min_img = min_functin(3, 3, copy.copy(img))
cv.imwrite("FiltroMaximo.jpg",max_img)
cv.imshow("FiltroMaximo.jpg",max_img)
cv.imwrite("FiltroMinimo.jpg",min_img)
cv.imshow("FiltroMinimo.jpg",min_img)


cv.waitKey(0)
cv.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:24:14 2022

@author: verom
"""

import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("filtrosp.jpg")

def gasuss_noise(image, mean=0, var=0.001):

    '''
                 Agregue ruido gaussiano
                 significar: significar
                 var: varianza
    '''
    
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)

    return out


def sp_noise(image,prob):


    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]

    return output


#  ruido de sal y pimienta, la relación de ruido es 0.02
out1 = sp_noise(img, prob=0.02)

#  ruido gaussiano con un valor medio de 0 y una varianza de 0.01
out2 = gasuss_noise(img, mean=0, var=0.01)


# Mostrar imagen
cv2.imwrite("PerroSYP.jpg",out1)
cv2.imshow("PerroSYP.jpg",out1)
cv2.imwrite("PerroGauss.jpg",out2)
cv2.imshow("PerroGauss.jpg",out2)
cv2.waitKey(0)
cv2.destroyAllWindows()


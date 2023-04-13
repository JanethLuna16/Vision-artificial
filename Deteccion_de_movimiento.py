# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:55:59 2022

@author: verom
"""


'''
import cv2
capture = cv2.VideoCapture(0)
while (capture.isOpened()):
    ret, frame = capture.read()
    cv2.imshow('webCam',frame)
    if (cv2.waitKey(1) == ord('s')):
        break
'''
import cv2
import numpy as np
video = cv2.VideoCapture(0)
i = 0 #contador para Captar el fondo de  la imagen
while True:
  ret, frame = video.read() #Las imagenes se almacenan en el frame
  if ret == False: break #  si no se pudo guarar imagen se rompe ciclo
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
  if i == 20: #asegurar que se capte bien la imagen 
    bgGray = gray  #imagen del fondo
  if i > 20:
    dif = cv2.absdiff(gray, bgGray) #operacion para diferencia de imagenes entre el fondo y el exterior
    _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY) #transformar imagen a binaria p>40 =255 area en blanco=movimiento

    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   # cv2.drawContours(frame, cnts, -1, (255,255,255),2)  
    #despreciar contornos pequeños , no representan movimiento
    for c in cnts:
      area = cv2.contourArea(c) #determinar area de pixeles
      if area > 9000: 
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2) #dibujar rectangulo si area>9000
  cv2.imshow('Frame',frame)
  i = i+1
  if cv2.waitKey(30) & 0xFF == ord ('q'):
   break
video.release()
cv2.destroyAllWindows()
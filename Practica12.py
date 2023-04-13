# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:54:52 2022

@author: verom
"""

import cv2

capture = cv2.VideoCapture(0)

while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):

        blur = cv2.blur(frame, (5, 5))

        bordesCanny = cv2.Canny(frame, 100, 200)
        CannyBlur = cv2.Canny(blur, 100, 200)
        
        cv2.imshow("Ventana", frame)
        cv2.imshow("Canny", bordesCanny)
        cv2.imshow("CannyBlur", CannyBlur)

        if (cv2.waitKey(1) == ord('a')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()

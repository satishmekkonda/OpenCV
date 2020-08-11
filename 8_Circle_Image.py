## Drawing Filled and Unfilled Circles on a Image via Mouse Clicks


import cv2
import numpy as np


def create_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 120, (0,0,255), thickness = 10)
        
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 120, (0,255,0), -1)
        
img = cv2.imread('Color Photo Pixelled.jpg')

cv2.namedWindow(winname = 'Bro')

cv2.setMouseCallback('Bro', create_circle)

while True:
    
    cv2.imshow('Bro', img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
    
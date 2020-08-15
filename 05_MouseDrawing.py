import cv2
import numpy as np


####################
##FUNCTION##
####################

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,255,0), -1)
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (255, 0, 0), -1)
        
cv2.namedWindow(winname = 'my_drwaing')

cv2.setMouseCallback('my_drawing', draw_circle)

#######################################
##Displaying Image with Open CV##
#######################################

img = np.zeros(shape=(512,512,3), dtype=np.int8)

while True:
    cv2.imshow('my_drawing', img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
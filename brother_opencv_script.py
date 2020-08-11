import cv2

img = cv2.imread('Color Photo Pixelled.jpg')

while True:
    cv2.imshow('Brother', img)
    
    ## If we've waited at leat 1ms AND we've pressed the ESC
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
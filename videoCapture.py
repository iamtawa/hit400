import numpy as np
import cv2

cap = cv2.VideoCapture('plate.mp4')

while True:
    ret, frame = cap.read()
    
    cv2.imShow('frame')
    
    if cv2.wait(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()


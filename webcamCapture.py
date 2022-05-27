import cv2
 
cap = cv2.VideoCapture('plate.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
while True:
    ret, img = cap.read()
    cv2.putText(img,str(fps) + " fps", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255,2) #0.5 is the font size , 255 the font color and 2 the thickness of the text
    cv2.imshow('Window',img)
 
 
    if cv2.waitKey(1) == 13:
        break
 
cap.release()
cv2.destroyAllWindows()
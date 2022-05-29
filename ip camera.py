import cv2

#IP Camera Information
scheme = '192.168.1.'
stream = '12'

#'101' is the last octet of the IP for the stream.
host = scheme+'101'
cap = cv2.VideoCapture('rtsp://'+host+':554/'+stream)

while True:
    _, frame = cap.read()
  
    #Place options to overlay on the video here.
    #I'll go over that later.
 
    cv2.imshow(('Camera'+str(camera_id)), frame)
 
    k = cv2.waitKey(0) & 0xFF
    if k == 27: #esc key ends process
        cap.release()
        break
cv2.destroyAllWindows()

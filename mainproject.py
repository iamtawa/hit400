import RPi.GPIO as GPIO
import time
import cv2

GREEN = 13
YELLOW = 19
RED = 26

PIN_TRIGGER = 11
PIN_ECHO = 18

#on and off functions
def liteon(pin,tiim):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(tiim)
def liteoff(pin,tiim):
    GPIO.output(pin,GPIO.LOW)
    time.sleep(tiim)
def captureImage():
    cap = cv2.VideoCapture('plate.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    while True:
        ret, img = cap.read()
        cv2.imshow('Window',img)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()    
    
def objectDetection():
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    print ("Waiting for sensor to settle")

    time.sleep(2)

    print ("Calculating distance")

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
      
    print ("Distance:",distance,"cm")
    
    if distance < 30 and liteon(26,10) == True:
        captureImage
        
    
        
    
    
    return
    
# Pin Setup:
GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme.


GPIO.setwarnings(False)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)



#for i in range(0,3):
while True:
        liteon(13,10)
        liteoff(13,.1)
        liteon(19,3)
        liteoff(19,.1)
        liteon(26,10)
        objectDetection()
        liteoff(26,.1)
        
print("done")
GPIO.cleanup()

          
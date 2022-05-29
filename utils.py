import RPi.GPIO as GPIO
import time
import cv2


from constants import *

# Pin Setup:
GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme.


GPIO.setwarnings(False)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)  # Red

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

# define the countdown func.
def countdown(pin, t):
    print('Begining Traffic light timer')
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        if pin == RED: # Calculate distance if traffic light is RED
            print(f'Red traffic light: ...checking for distance {timer} remaining')
            distance = object_detection()
            if distance < MIN_DETECTION_DISTANCE:
                capture_image()
        time.sleep(1)
        t -= 1
      
    print('Ended Traffic light timer')
  

def capture_image():
    cap = cv2.VideoCapture('plate.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    while True:
        ret, img = cap.read()
        cv2.imshow('Window',img)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()    

    return


def object_detection():
    GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme.
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

    return distance



#on and off functions
def liteon(pin,tiim):
    GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme.
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(RED, GPIO.OUT)  # Red

    GPIO.output(pin,GPIO.HIGH)
    countdown(pin, int(tiim))
    # time.sleep(tiim)

def liteoff(pin,tiim):
    GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme.
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(RED, GPIO.OUT)  # Red
    GPIO.output(pin,GPIO.LOW)
    time.sleep(tiim)
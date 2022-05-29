import RPi.GPIO as GPIO
import time
import cv2


from constants import *


# define the countdown func.
def countdown(pin, t):
    print(f'[{get_traffic_light_color_from_pin(pin)}] Begining Traffic light timer')
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
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while(True):
        # Capture the video frame by frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows() 


def object_detection():
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
    GPIO.output(pin,GPIO.HIGH)
    countdown(pin, int(tiim))
    # time.sleep(tiim)

def liteoff(pin,tiim):
    GPIO.output(pin,GPIO.LOW)
    time.sleep(tiim)



def get_traffic_light_color_from_pin(pin):
    if pin == GREEN:
        color = "GREEN"
    if pin == YELLOW:
        color = "YELLOW"
    if pin == RED:
        color = "RED"
    return color
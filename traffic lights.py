import RPi.GPIO as GPIO
import time, threading

GREEN = 13
YELLOW = 19
RED = 26

PIN_TRIGGER = 11
PIN_ECHO = 18

pins = [26, 19, 13]

pinIndex = 0
currentlyRed = False

seconds = 10


def switchLights():
    global pinIndex
    global seconds
    liteoff(pins[pinIndex])
    pinIndex += 1
    if pinIndex == 3:
        pinIndex = 0
        
    if pinIndex == 1:
        seconds = 5
    else:
        seconds = 10
    
    liteon(pins[pinIndex])
    
    currentTime = time.time()
    
    
    while pinIndex == 0:
        camtrigger()
        currentTimeNow = time.time()
        
        print("Start time: ", currentTime)
        print("Now: ", currentTimeNow)
        print("Difference: ", currentTimeNow - currentTime)
        if (currentTimeNow - currentTime) > 10:
            print("Breaking")
            break
    


#on and off functions
def liteon(pin):
    GPIO.output(pin,GPIO.HIGH)
    #time.sleep(tiim)
def liteoff(pin):
    GPIO.output(pin,GPIO.LOW)
    #time.sleep(tiim)
def camtrigger():
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    #print ("Waiting for sensor to settle")

    time.sleep(2)

    #print ("Calculating distance")

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
    print("RED: ", GPIO.output(26,GPIO.HIGH))
    print("iii", GPIO.input(26))
    if distance < 30 and GPIO.input(26) == 1:
       print("trigger camera to capture an image")
       
    print("Done exiting ...")
       
    return

# Pin Setup:
#GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme.
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

while True:
    switchLights()
    time.sleep(seconds)

         
print ("Done")
GPIO.cleanup()
         
         
    
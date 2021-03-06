import RPi.GPIO as GPIO
import time
import cv2

from  utils import liteon, liteoff

from constants import *


def main():
    while True:
        liteon(13,10)
        liteoff(13,.1)
        liteon(19,3)
        liteoff(19,.1)
        liteon(26,10)
        liteoff(26,.1)

        
print("done")
GPIO.cleanup()


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme.
    GPIO.setwarnings(False)
    # Traffic light pins
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(RED, GPIO.OUT)  # Red
    # Ultrasonic pins
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    main()
  
          
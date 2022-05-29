# import the time module
import time

from .constants import RED, MIN_DETECTION_DISTANCE
from .utils import object_detection, capture_image

  
# define the countdown func.
def countdown(pin, t):
    print('Beging Traffic light timer')
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
  

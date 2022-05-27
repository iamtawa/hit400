#firebaseconnections

from firebase import firebase
import RPi.GPIO as GPIO
import dht11
import time

url=’paste_your_database_url_here’

firebase = firebase.FirebaseApplication(url)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
instance = dht11.DHT11(pin=2)

while True:
result = instance.read()
if result.is_valid():
print(“Temp: %d C” % result.temperature + ‘ ‘ +”Humid:%d %%”% result.humidity)
temp = firebase.put(“Weather”,”Temp”, result.temperature)
humid = firebase.put(“Weather”, “Humid”, result.humidity)
time.sleep(1)


##anothersnippet

# This code should be used with every script that you will be using to connect to the Firebase database.
import pyrebase
from firebase import firebase
config = {
  # You can get all these info from the firebase website. It's associated with your account.
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
.
.
.
.


##another one

"""
Tutorial: Send Data to Firebase Using Raspberry Pi
Hardware:
– Raspberry Pi 4 Model B
– Maker pHAT
– MLX90614
References:
– https://circuitpython.readthedocs.io/projects/mlx90614/en/latest/
– https://github.com/thisbejim/Pyrebase
"""

import time
import board
import busio as io
import adafruit_mlx90614
import pyrebase

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

config = {
  "apiKey": "database-secret",
  "authDomain": "project-id.firebaseapp.com",
  "databaseURL": "https://database-url.firebaseio.com",
  "storageBucket": "project-id.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")
print("—————————————-")
print()

while True:
  ambientString = "{:.2f}".format(mlx.ambient_temperature)
  objectString = "{:.2f}".format(mlx.object_temperature)

  ambientCelsius = float(ambientString)
  objectCelsius = float(objectString)

  print("Ambient Temp: {} °C".format(ambientString))
  print("Object Temp: {} °C".format(objectString))
  print()

  data = {
    "ambient": ambientCelsius,
    "object": objectCelsius,
  }
  db.child("mlx90614").child("1-set").set(data)
  db.child("mlx90614").child("2-push").push(data)

  time.sleep(2)
  
  
#   ##
import serial
import time
import requests
import json

firebase_url = 'https://testing1639.firebaseio.com'

#Connect to Serial Port for communication
ser = serial.Serial('/dev/ttyUSB0', 9600)

#Setup a loop to send temperature values at fixed intervals in seconds
fixed_interval = 2

while 1:
    try:
         #Temperature value obtained from Arduino + LM35 Temp Sensor
         temperature_c = ser.readline()
         #Current time and date
         time_hhmmss = time.strftime('%H:%M:%S')
         date_mmddyyyy = time.strftime('%d/%m/%Y')

         #Current location name
         temperature_location = 'Mumbai-Kandivali' ;

         print temperature_c + ',' + time_hhmmss + ',' + date_mmddyyyy + ',' + temperature_location

         #Insert record
         data = {'date':date_mmddyyyy,'time':time_hhmmss,'value':temperature_c}

         result = requests.post(firebase_url + '/' + temperature_location + '/temperature.json', data=json.dumps(data))

         #Insert record
         print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
         time.sleep(fixed_interval)

    except IOError:
        print('Error! Something went wrong.')
        time.sleep(fixed_interval)
##gsm snippet

import serial
import time

receiverNum = "+263787226381"
'''sim800l = serial.Serial(
port='/dev/serial1',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)'''
sim800l = serial.Serial("/dev/ttyUSB0",9600, timeout=0.5)
sim800l.flush()

sms = "hi, mr tee. you owe us 10bucks"
time.sleep(1)
print ("pass")
#sim800l.write(b"AT")
sim800l.write(b'AT+CMGF=1\n')
print ("pass")
print (sim800l.read(24))
time.sleep(1)
#cmd1 = "AT+CMGS=\" "+str(receiverNum)+"\"\n"
cmd1 = "AT+CMGS=\+263787226381\\n"
str1 = bytes(cmd1, 'utf-8')
sim800l.write(str1)
print (sim800l.read(24))
time.sleep(1)
sim800l.write(sms.encode())
#sim800l.write(b'\x1A')
sim800l.write(chr(26).encode())
print (sim800l.read(24))

'''

#gsm code
import serial as io
import time 
gsm = io.Serial("/dev/ttyUSB0",9600, timeout=0.5)
gsm.flush()

def sleep(a):
    time.sleep(a)
 
def sendSms(msg):
    print("Sending SMS\n")
    gsm.write(b'AT+CMGF=1\r\n')
    sleep(0.5)
    gsm.write(b'AT+CMGS=\"')
    serialcmd = args["mobile"]
    gsm.write(serialcmd.encode())
    gsm.write(b'\"\r\n')
    sleep(0.5)
    data = msg
    gsm.write(data.encode())
    gsm.write(b'\x1A')
    sleep(3)
 
sendSms("Hello mevihub.com")

'''

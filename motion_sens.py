import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

pir = 19 
Relay1 = 4

GPIO.setup(pir,GPIO.IN)
GPIO.setup(Relay1,GPIO.OUT)

while True:
    if GPIO.input(pir):
        GPIO.output(Relay1,False)
    else:
        GPIO.output(Relay1,True)
    sleep(0.5)

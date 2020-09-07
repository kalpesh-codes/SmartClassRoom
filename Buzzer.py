import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

buzz = 26


GPIO.setup(buzz,GPIO.OUT)


GPIO.output(buzz,False)

def ring(cnt):
    for i in range(cnt):
        GPIO.output(buzz,True)
        sleep(.1)
        GPIO.output(buzz,False)
        sleep(.1)

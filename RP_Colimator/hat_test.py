import RPi.GPIO as GPIO
from time import *

led_pin = 20,13,6,25
but_pin = 17

 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
[GPIO.setup(i, GPIO.OUT) for i in led_pin]
GPIO.setup(but_pin, GPIO.IN)

def led_set(ix):
    for i in led_pin:
        GPIO.output(i, GPIO.LOW)       
    GPIO.output(led_pin[ix], GPIO.HIGH)

i = 0 
while True:
    led_set(i)
    i = (i+1)%4
    sleep(0.5)

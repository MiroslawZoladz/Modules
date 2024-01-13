from machine import Pin
from time import sleep_ms

p = Pin(0, Pin.OUT)
while(1):
    input()
    p.high()
    sleep_ms(10)
    p.low()

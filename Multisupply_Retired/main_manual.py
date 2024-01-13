from machine import Pin, SoftI2C
from display import Display

sda=Pin(16)
scl=Pin(17)
i2c=SoftI2C(sda=sda, scl=scl, freq=100000)

display = Display(i2c)

display.show(0, 1.234, 5.678)

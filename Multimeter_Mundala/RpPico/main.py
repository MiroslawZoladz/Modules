HELP = "m: read temp [C]\n"\
            "cnt : continous mode\n"\
            "h : help\n"

from machine import Pin,SoftSPI
from max31865 import MAX31865
from display import Display
import time

RTD_NOMINAL = 100
RTD_REF = 430
RTD_WIRES = 4

sck = Pin(10, Pin.OUT)
miso = Pin(11, Pin.OUT)
mosi = Pin(12, Pin.IN)
cs = Pin(13, Pin.OUT, value = 1)
spi = SoftSPI(baudrate = 100000, sck=sck, mosi=mosi, miso=miso)

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=100000)

max31865 = MAX31865(spi, cs, wires = RTD_WIRES)
display = Display(i2c)

while True:  
    
    command = input("Give command:")
#     command = 'cnt'
    tokens = command.split()
    try:
        if tokens[0] == 'm':
            x = 12/0
            print(f"{max31865.temperature}")
            display.show_temp(max31865.temperature)
        elif tokens[0] == 'cnt':
            while True:
                print(f"{max31865.temperature}")
                display.show_temp(max31865.temperature)
                time.sleep(1)
        elif tokens[0] == 'h':
            print(HELP)
        else:
            print(HELP)
    except:
        print('exception')
        
        
from machine import Pin
from machine import lightsleep

led = Pin(25, Pin.OUT)
led.high()
lightsleep(500)
#led.low()

div_bits = None
reset = None 

def set_div(div):
    global div_bits, reset
    
    led.toggle()
    
    if not div_bits:
        div_bits = [Pin(i, Pin.OUT) for i in range(13)]
        reset = Pin(12, Pin.OUT)

    for pin in range (12):
        if (div>>(11-pin))&(1<11):
            div_bits[pin].high()
            #print(pin,1)
        else:
            div_bits[pin].low()
            #print(pin,0)
            
    reset.low()
    lightsleep(100)
    reset.high()
    lightsleep(100)
    reset.low()

set_div(0x63)
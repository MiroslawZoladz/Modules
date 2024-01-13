from machine import Pin, PWM, SoftI2C
from board import Board
from keyboard import keyboard
from display import Display

pwm = PWM(Pin(10))
pwm.freq(10000)
pwm.duty_u16(pow(2,16)//10)

sda=Pin(20)
scl=Pin(21)
i2c=SoftI2C(sda=sda, scl=scl, freq=400000)

board = Board(i2c)
display = Display(i2c)
keyboard = keyboard()
channel = 0

while True:
    butt_read = keyboard.read()
    if butt_read == 'UP' and channel < 4:
        channel += 1
        board.set_channel(channel)
    elif butt_read == 'DOWN' and channel > 0:
        channel -= 1
        board.set_channel(channel)
    elif butt_read == 'RIGHT':
        board.inc()
    elif butt_read == 'LEFT':
        board.dec()
    elif butt_read == 'MIDDLE':
        board.save()
    else:
        pass
    
    board.set_param('v')
    voltage = board.measure()

    board.set_param('c')
    current = board.measure()
    if current > 10000:
        current = 0
    
    display.show(channel, voltage/1000, current/1000)

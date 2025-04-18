import RPi.GPIO as GPIO
import curses
from time import sleep

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

curses.KEY_ENTER = 10
         
def main(stdscr):

        led_pointer = 0

        curses.curs_set(0)

        while True:
                # legend
                stdscr.addstr(0, 0, "CONTROLS:")
                stdscr.addstr(1, 0, "ARROW UP,  ARROW DOWN,  ENTER")
                
                # debug
                stdscr.addstr(4, 0, "led_pointer: " + str(led_pointer))

                # User input control
                user_char = stdscr.getch()

                if (user_char == curses.KEY_DOWN):
                        led_pointer += 1
                        if (led_pointer == 4): led_pointer = 0
                elif (user_char == curses.KEY_UP):
                        led_pointer -= 1
                        if (led_pointer < 0): led_pointer = 3
                elif (user_char == curses.KEY_ENTER):
                    pass
                            
                led_set(led_pointer)
                
                stdscr.erase()
                
curses.wrapper(main)
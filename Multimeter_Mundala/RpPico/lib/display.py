import machine
from ssd1306 import SSD1306_I2C
import framebuf
import freesans24
import freesans28
import freesans46
import writer

class Display:
    
    __CHAN_NAMES = {0:'core', 1:'peri', 2:'ddm', 3:'dda', 4:'disc'}
    
    def __init__(self, i2c):    
        self._oled = SSD1306_I2C(128, 64, i2c)
        self._font_writer = writer.Writer(self._oled, freesans46)
        

    def string(self, s):
        self._oled.fill(0)
        self._font_writer.set_textpos(10, 10)
        self._font_writer.printstring(s)
        self._oled.show()

            
            
            
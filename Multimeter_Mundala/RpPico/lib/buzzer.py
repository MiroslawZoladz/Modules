import time

class Buzzer:
    
    def __init__(self, pin):
        self._buzz_pin = pin

    def beep(self, sec):
        for i in range(sec*1000):
            self._buzz_pin.value(not self._buzz_pin.value())
            time.sleep(0.001)
            
        
        
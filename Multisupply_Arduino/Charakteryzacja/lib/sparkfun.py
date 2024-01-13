import serial

class Sparkfun:
    com_nr=14    
    
    def set(self, I_mA):
        with serial.Serial(port=f"COM{self.com_nr}", baudrate=9600, bytesize=8,timeout=1, stopbits=serial.STOPBITS_ONE) as com:
            com.write((f'{I_mA/1000:0.3f}\r').encode())
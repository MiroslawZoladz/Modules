import serial

class Rigol:
    com_nr=33
                
    def cmd(self, cmd):
        with serial.Serial(port=f"COM{self.com_nr}", baudrate=9600, bytesize=8,timeout=1, stopbits=serial.STOPBITS_ONE) as com:
            com.write((cmd+'\n').encode())
            _ =com.readline().decode('utf-8').strip()
            if 'err' in _:
                return 'error'
            else:
                _ = _.replace('ok','')
                if _:            
                    return _
                else:
                    return 'ok'   
                
    def measure(self):
            self.cmd(f':function:{self.mode}:dc') 
            r = self.cmd(f':measure:{self.mode}:dc?')[1:]
            while r=='E' :
                r = self.cmd(f':measure:{self.mode}:dc?')[1:]
            return 1000*float(r)
        

class RigolVoltage(Rigol):
        def __init__(self):
            self.mode = 'voltage'
   
 
class RigolCurrent(Rigol):
        def __init__(self):
            self.mode = 'current'
import serial, time

class Board:
    com_nr= 32 #30
    channel=0 #4
    
    def __init__(self):
        self.cmd(f'ch {self.channel}')
                
    def cmd(self, cmd):
        with serial.Serial(port=f"COM{self.com_nr}", baudrate=9600, bytesize=8,timeout=1, stopbits=serial.STOPBITS_ONE) as com:
            com.write((cmd+'\r').encode())
            _ =com.readline().decode('utf-8').strip()
            if 'err' in _:
                return 'error'
            else:
                _ = _.replace('ok','')
                if _:            
                    return _
                else:
                    return 'ok'
                
    def config(self,config_line):
            for token in filter(bool,map(lambda s: s.strip(),config_line.split(' '))):
                name, value = map(lambda s: s.strip(),token.split('='))
                if 'err' in self.cmd(f'g {name} {int(value,0)}'):
                    return 'error'
            return 'ok'          

    def measure(self):
            return float(self.cmd('m'))
    
    def callib(self,val):
            self.cmd(f'l {val}')
            time.sleep(1)            
            return self.cmd(f'l {val}')            


class MCP4022(Board):
    def set(self,rezistance):        
        return self.cmd(f's {rezistance}')
    

class INA219_Voltage(Board):
    
    def __init__(self):
        super().__init__()
        self.cmd('v')


class INA219_Current(Board):
    
    def __init__(self):
        super().__init__()
        self.cmd('c')


        
 
        
        
    


     
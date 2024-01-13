import serial

class Multisupply:
    def __init__(self,com_nr=1):
        self.comm = serial.Serial(f'Com{com_nr}',115200,timeout=1)
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.comm.close()
        
    def cmd(self,cmd):
               
        self.comm.write(cmd.encode('UTF-8')+b'\r\n')
        self.comm.flushOutput()
        
        res = list()
        while True:
            _ = self.comm.readline().decode("utf-8").strip()
            res.append(_)
            if _ == 'ok':
                return res[1]
            elif 'err' in _:
                return 'error'                

    def enable_sections(self):
        self.cmd('sea')
        
    def disable_sections(self):
        self.cmd('sda')            
        
    def get_sections_state(self):
        d = dict()

        # potentiometer
        l = list()
        for i in range(5):     
            self.cmd(f'sch {i}')
            l.append(self.cmd('spg'))
        d['pot']=l
        
        # U,I
        for param_name, param_code in ('voltage','sv'),('current','si'):
            self.cmd(param_code)
            l = list()
            for i in range(5):     
                self.cmd(f'sch {i}')
                l.append(float(self.cmd('sm'))/1000)
            d[param_name]=l
            
        return d      
    
    def pot_inc(self,channel):
        self.cmd(f'sch {channel}')
        self.cmd('spi')
        
    def pot_dec(self,channel):
        self.cmd(f'sch {channel}')
        self.cmd('spd')        
        
    def hv_on(self):
        self.cmd('hve')        

    def hv_off(self):
        self.cmd('hvd')  
        
    def save(self):
        self.cmd('ss')
        
# reset
        
    def reset_ctl(self):
        self.cmd('rst')
    
# callibration voltage
    
    def call_enable(self):
        self.cmd('oe')
        
    def call_set_active_ch(self,ch): # n/p
        d = {'n':'0','p':'1'}
        self.cmd('och '+ d[ch])
        
    def call_set_voltage(self,v): #[V]
        self.cmd(f'ov {v:0.3f}')
    
    def macro_vcall_set(self,vn,vp):        
        self.call_enable()
        for label, voltage in (('n',vn),('p',vp)):
            self.call_set_active_ch(label)
            self.call_set_voltage(voltage)

# v_in voltage
    
    def vin_get(self):
        self.cmd('ich 0')
        return self.cmd('iv')

# strobe
    
    def strobe_set(self,f,p): #f in kHz, p in %
        self.cmd('pe')
        self.cmd(f'pf {f}')
        self.cmd(f'pp {p}')
        

"""        
pe: enable()
pd: disable()
pf: freq_set(int(*arg))
pp: pwm_set(int(*arg))
"""
        

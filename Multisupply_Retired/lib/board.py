from mcp4021 import MCP4021
from ina219 import INA219_Voltage, INA219_Current

class channel:
    def __init__(self, pot, meters):
        self.pot = pot
        self.meters = meters
        
class Board:
    
    __MAX_CHANNEL_NR = 5
    
    __channel_cs_numbers = [18, 22, 28, 27, 26] # [26, 27, 28, 22, 18]
    __channel_addresses = [0x44, 0x43, 0x42, 0x41, 0x40]
        
    def __init__(self, i2c):
        
        self.channels = []
        for channel_cs_nr, channel_addr in zip(self.__channel_cs_numbers, self.__channel_addresses):
            p = MCP4021(channel_cs_nr)
            m = {'c':INA219_Current(i2c, channel_addr), 'v':INA219_Voltage(i2c, channel_addr)}
            self.channels.append(channel(pot = p, meters = m))
        
        self._cahnnel = 0
        self._param = 'v'
        self.current_pot = self.channels[self._cahnnel].pot
        self.current_meter = self.channels[self._cahnnel].meters[self._param]
        
    def set_channel(self, chan_nr):
        self._cahnnel = chan_nr
        self.current_pot = self.channels[chan_nr].pot
        self.current_meter = self.channels[chan_nr].meters[self._param]
    def set_param(self, param):
        self._param = param
        self.current_meter = self.channels[self._cahnnel].meters[param]        
    def set(self, value):
        self.current_pot.set(value)
    def inc(self):
        self.current_pot.inc(1)
    def dec(self):
        self.current_pot.dec(1)
    def save(self):
        for chan in self.channels:
            chan.pot.save()
    def measure(self):
        return self.current_meter.measure()
    def callib(self, value):
        self.current_meter.callib(value)
    def config(self, name, value):
        self.current_meter.config(name, value)
    def coeff(self):
        return self.current_meter.read_coefficient()
    def raw(self):
        return self.current_meter.measure_raw()
        
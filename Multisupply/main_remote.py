HELP =""" Commands

# supply
sch: set current channel
sv : set voltage as current electrical parameter
si : set current as current electrical parameter

sps: set voltage potentiometer (0-63)
spg: pot. get
spi: pot. inc
spd: pot. dec

sea: enable all channels
sda: disable all channels
sech : enable current channel
sm : measure current param (U/I) at current channel
ss: save volatge settings

# suply service
sc : callibration in mili
sr : read register
sf : read coefficient
sg : [brng/pg/badc] config device

Analog Outputs (unit: V)
oe  : enable all channels
od  : disable all channels
och : set curent channel
ov  : set voltage
omin: set max value on all dac-s
omax: set min value on all dac-s
oc  : callibrate curent channel, arguments: voltage at omin, voltage at omax 

Analog Inputs (unit: V)   
ich : set curent channel
iv  : get voltage from current channel
iva : get voltage from all channels
ivapp:get voltage from all channels, nice formated
ic  :  callibrate curent channel, arguments: adc index, voltage at ch0-virtual (ch1 phys), ch0 phys must be connected to gnd 

# hv
hve : enable
hvd : disable
hvs : save

# fpga
rst : fpga reset
"""

from machine import Pin, PWM, SoftI2C
from display import Display
from board import Board
from analog_outputs import AnalogOutputs
from analog_inputs   import AnalogInputs
from HV import HV
from config_jumpers import JMP
from pwm import Pwm

pin = Pin(25, Pin.OUT) # led
pin.on()
def fpga_reset():
    pin.off()
    pin.on()

sda=Pin(17)
scl=Pin(18)
i2c=SoftI2C(sda=sda, scl=scl, freq=100000)

disp = Display(i2c)

board = Board(i2c)
ao = AnalogOutputs()
ai = AnalogInputs()
hv = HV(disable=True)
pwm = Pwm()

disp.show_str('remote\ncontrol')

while True:
            
    try:
        command = input("")
        tokens = command.split()
        if not tokens:
            print(HELP)
            continue
        cmd, arg  = tokens[0], [float(s) for s in tokens[1:]]
        
        # supply
        if   cmd == 'sea': board.enable_all()
        elif cmd == 'sda': board.disable_all()
        elif cmd == 'sech' : board.enable_channel()
        elif cmd == 'sch': board.set_channel(int(*arg))
        elif cmd == 'sv' : board.set_param('v')
        elif cmd == 'si' : board.set_param('c')
        elif cmd == 'sps' : board.set_pot(int(*arg))
        elif cmd == 'spg' : print(board.get_pot())
        elif cmd == 'spi' : board.inc()
        elif cmd == 'spd' : board.dec()
        elif cmd == 'sm' :            
            val = board.measure()
            if val>10000:
                val  = 0
            print(val)
        elif cmd == 'ss': board.save()            
        
        elif cmd == 'sc': board.callib(int(*arg))
        elif cmd == 'sg': board.config(arg[0], int(arg[1]))
        elif cmd == 'sf': print(board.coeff())
        elif cmd == 'sr': print(board.raw())
        
        # analog outputs
        elif cmd == 'oe'  : ao.enable()
        elif cmd == 'od'  : ao.disable()
        elif cmd == 'och' : ao.set_channel(int(*arg))
        elif cmd == 'ov'  : ao.set_voltage(float(*arg))
        elif cmd == 'omin': ao.min()
        elif cmd == 'omax': ao.max()
        elif cmd == 'oc'  : ao.callib(*arg)        
        
        # analog inputs
        elif cmd == 'ich'  : ai.set_channel(int(*arg))
        elif cmd == 'iv'   : print(f'{ai.get_voltage(*arg):0.3f}')
        elif cmd == 'iva'  : print(' '.join([f'{v:0.3f}' for v in ai.get_voltage_all()]))
        elif cmd == 'ivapp': [print(f'ch_{ch_i:02d}: {v:0.3f}') for ch_i,v in enumerate(ai.get_voltage_all())] #[print(f'ch_{ch_i:02d}: {v:0.3f}') for ch_i,v in enumerate(ai.get_voltage_all())]
        elif cmd == 'ic'   : ai.callib(*arg)
        
        # HV
        elif cmd == 'hve': hv.enable()
        elif cmd == 'hvd': hv.disable()
        
        # PWM
        elif cmd == 'pe': pwm.enable()
        elif cmd == 'pd': pwm.disable()
        elif cmd == 'pf': pwm.freq_set(int(*arg))
        elif cmd == 'pp': pwm.pwm_set(int(*arg))
        
        # FPGA
        elif cmd == 'rst': fpga_reset()
        
        else: print(HELP)
        
        print('ok')

    except Exception as e:
        print('Error',e)


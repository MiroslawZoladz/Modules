from pinout import Pinout
from machine import Pin
pin_rmt_ctl = Pin(Pinout.JMP_RMT_CTL, Pin.IN,Pin.PULL_UP)


if pin_rmt_ctl.value()==0:# jmp.rmt_ctl:
    import main_remote
else:
    import main_manual
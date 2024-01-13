from machine import Pin, UART
import onewire, ds18x20, time
from display_ssd1306_i2c import Display

disp = Display(sda_pin_nr=20,scl_pin_nr=21,font_size=10)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1),timeout = 2_000_000_000, timeout_char = 2_000_000_000) # 2 dni


disp.print_list(['Restarted'])

msg_l = []
while(True):
    l = uart.readline()
    if l==None: continue
    l = l.decode("utf-8")
    l = l.strip()
        
    if 'Waiting for PHY' in l:
        msg_l.append('Waiting for PHY')
    elif 'speed' in l:
        speed = l.split(':')[-1]
        msg_l.append('Speed: '+speed.strip())
    elif 'IP' in l:
        msg_l.append('IP: '+l.split(' ')[-1])
    elif 'port' in l:
        msg_l.append('Port: '+l.split(' ')[-1])
    elif 'error' in l:
        msg_l.append('Error')
        
    disp.print_list(msg_l)
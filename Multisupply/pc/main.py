import msvcrt, os, time
from tabulate import tabulate
from supply_lib import Multisupply

def redraw(sp):   
    channel_names = 'core','peri', 'ddm', 'dda', 'discr'
    cursor_l = ['->' if i==current_ch else '  ' for i, _ in enumerate(channel_names)]    
    ch_names = [n.upper() if i==current_ch else n for i, n in enumerate(channel_names)]
    supp_state = sp.get_sections_state()
    table = tabulate(zip(cursor_l,ch_names,supp_state['voltage'],supp_state['current'],supp_state['pot']), headers=['','','V','A','Pot'],floatfmt=".3f")
    
    
    os.system('cls')
    print()
    print(table)
    
    hlp = """ \n
** HELP **
e: enable 
d: disable
h: HV ON
H: HV OFF
s: save
r: reset
space: refresh
    """
    print(hlp)

# ****** MAIN *******
    # _ = sp.get_sections_state()
current_ch = 0


with Multisupply(35) as  sp:
    while(True):
        redraw(sp)
        c = msvcrt.getch()
        if c == b'\xe0':
            c = msvcrt.getch()
            if c==b'M': #right
                sp.pot_inc(current_ch)
                time.sleep(0.3)                
            if c==b'K': #left
                sp.pot_dec(current_ch)
                time.sleep(0.3)                             
            if c==b'H': #up
                if current_ch>0:
                    current_ch -= 1                
            if c==b'P': #down
                if current_ch<4:
                    current_ch += 1
                    
        elif c == b'e':
            sp.enable_sections()
            time.sleep(0.5) 
            
        elif c == b'd':
            sp.disable_sections()
            time.sleep(0.5) 
            
        elif c == b's':
            sp.save()
            os.system('cls')
            print('saved')
            time.sleep(0.5) 
            
        elif c == b'h':
            sp.hv_on()
            os.system('cls')
            print('HV ON')
            time.sleep(0.5) 
            
        elif c == b'H':
            sp.hv_off()
            os.system('cls')
            print('HV OFF')
            time.sleep(0.5) 
        
        elif c == b'r':
            sp.reset_ctl()
            os.system('cls')
            print('Reset ctl')
            time.sleep(0.5)         
            
            

        
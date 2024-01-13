from supply_lib import Multisupply

with Multisupply(35) as  sp:   
    sp.macro_vcall_set(0.950,0.250)
    v = float(sp.vin_get())
    print(v)
    
    sp.strobe_set(10,10)

import sys
sys.path.append('../lib')
from machine import SoftI2C
from ina219 import INA219_Current,INA219_Voltage

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=SoftI2C(sda=sda, scl=scl, freq=400000)

devices = i2c.scan()
 
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
 
  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))


ina_cur = INA219_Current(i2c, 0x40)

print("Shunt voltage: %i " % ina_cur.measure())
# print('Scan i2c bus...')
# devices = i2c.scan()
#  
# if len(devices) == 0:
#   print("No i2c device !")
# else:
#   print('i2c devices found:',len(devices))
#  
#   for device in devices:  
#     print("Decimal address: ",device," | Hexa address: ",hex(device))

# # ina_vol.config('sadc', 0xF)
# ina_cur.config('sadc', 0xF)
# 
# # ina_vol.config('badc', 0xF)
# ina_cur.config('badc', 0xF)
# 
# # ina_vol.config('pg', 0x0)
# ina_cur.config('pg', 0x0)
# 
# # ina_vol.config('brng', 0x0)
# ina_cur.config('brng', 0x0)
# 
# # print("Bus voltage raw: %i " % ina_vol.measure_raw())
# print("Shunt voltage raw: %i " % ina_cur.measure_raw())
# 
# # print("Bus voltage: %i " % ina_vol.measure())
# print("Shunt voltage: %i " % ina_cur.measure())
# 
# print("Coefficient: %f" % ina_cur.read_coefficient())
# 
# # ina_vol.callib(2)
# ina_cur.callib(32)
# 
# # print("%f" % ina_vol.read_coefficient())
# print("Coefficient: %f" % ina_cur.read_coefficient())

# print("Bus voltage: %i " % ina_vol.measure())
# print("Shunt voltage: %i " % ina_cur.measure())
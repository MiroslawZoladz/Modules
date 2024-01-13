import machine
sda=machine.Pin(17)
scl=machine.Pin(18)
i2c=machine.SoftI2C(sda=sda, scl=scl, freq=100000)
 
print('Scan i2c bus...')
devices = i2c.scan()
 
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
 
  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
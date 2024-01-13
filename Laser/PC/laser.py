import serial

def _write_commmand(cmd):
    global comm
    print(cmd)
   
    comm = serial.Serial('Com5',115200,timeout=1)
    # time.sleep(0.5)
    comm.flushInput()
    
    comm.write(cmd.encode('UTF-8')+b'\r\n')
    comm.flushOutput()
    comm.readline()
    comm.read(3) #len(cmd)+2+3+1)
    
    comm.close()

   
def set_div(div):
   _write_commmand(f"set_div({div})")


set_div(0xA53)
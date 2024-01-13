from my_serial import my_serial,read
import numpy as np

import matplotlib.pyplot as plt
import time

# %matplotlib qt
# %matplotlib inline

temp_l=list()

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

x = list(range(1))
y = list(range(1))
line1, = ax.plot(x,y,'-p')
plt.grid()


COM = 49

with my_serial(COM) as sr_camera:
    while True:
        s = read(sr_camera)
        temp_l.append(float(s[4:8]))
        t_l = list(range(len(temp_l)))
        plt.xlim(0,len(temp_l))
        plt.ylim(min(temp_l)-3,max(temp_l)+3)
        line1.set_xdata(t_l)
        line1.set_ydata(temp_l)
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.1)
        



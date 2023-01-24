# Name: Paolo Acosta
# ID: 013117104

#imported libraries
import math as m
import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt

#creates acceleration function
def acceleration(t):
    return (22000/((t-74)**2 + 500))

#creates HIC function
def hic(d, t):
    return (d*pow(1/d*integ.quad(acceleration,t,t+d)[0], 2.5)/1000)

#plots the acceleration 
time = [x for x in range(160)] # tv is in mSec
acc = [acceleration(x) for x in time]
plt.plot(time, acc)
plt.title('Acceleration (m/s**2) vs Time (ms)')
plt.xlabel('time (ms)')
plt.ylabel('acceleration (m/s**2)')
plt.grid()
plt.show()

#plots the HIC for when d = 50 and d = 35
htd50 = [hic(50,t) for t in time]
htd35 = [hic(35,t) for t in time]
plt.plot(time, htd50,'b')
plt.plot(time, htd35,'g')
plt.grid()
plt.title('HIC with airbag case for d=50')
plt.xlabel('time (ms)')
plt.ylabel('HIC')
plt.show()

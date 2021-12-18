#Paolo Acosta
#013117104
import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO

m = GEKKO()

# integration time points
m.time = np.linspace(0,100)

# constants
rate1 = 0.5 #rate of eru to icu
rate2 = 0.7 #rate to exit icu

nurses_eru = 20 #number of nurses in eru
nurses_icu = 10 #number of nurses in icu

ventilators = 2 #number of ventilators
clean = .5 #time to clean ventilators
use = 2 #time to clean
diagnosis = .5 #time to diagnose
Ac_eru = nurses_eru/diagnosis     
Ac_icu = nurses_icu/(ventilators*(use + clean))
# inflow
qin1 = 10  # people/hour

# variables
eru = m.Var(value=0,lb=0,ub=10)
icu = m.Var(value=0,lb=0,ub=5)
overflow1 = m.Var(value=0,lb=0)
overflow2 = m.Var(value=0,lb=0)

# outflow equations
qin2 = m.Intermediate(rate1 * eru**0.5)
qout1 = m.Intermediate(qin2 + overflow1)
qout2 = m.Intermediate(rate2 * icu**0.5 + overflow2)

# mass balance equations
m.Equation(Ac_eru*eru.dt()==qin1-qout1)
m.Equation(Ac_icu*icu.dt()==qin2-qout2)

# minimize overflow
m.Obj(overflow1+overflow2)

# set options
m.options.IMODE = 6 # dynamic optimization

# simulate differential equations
m.solve()

# plot results
plt.figure(1)
plt.plot(m.time,eru,'b-')
plt.plot(m.time,icu,'r--')
plt.xlabel('Time (hrs)')
plt.ylabel('Patients')
plt.legend(['ERU','ICU'])
plt.show()
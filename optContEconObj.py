'''
Original Form

$\max_{u(t)} \int_0^{10} \left(E-\frac{c}{x}\right) u \, U_{max} \, dt$

$\mathrm{subject \; to}$

$\frac{dx}{dt}=r \, x(t) \left(1-\frac{x(t)}{k}\right)-u \, U_{max}$

$x(0) = 70$

$0 \le u(t) \le 1$

$E=1, \, c=17.5, \, r=0.71$

$k=80.5, \, U_{max}=20$

Equivalent Form for GEKKO

$\min_{u(t)} -J\left(t_f\right)$

$\mathrm{subject \; to}$

$\frac{dx}{dt}=r \, x(t) \left(1-\frac{x(t)}{k}\right)-u \, U_{max}$

$\frac{dJ}{dt} = \left(E-\frac{c}{x}\right) u \, U_{max}$

$x(0) = 70$

$J(0) = 0$

$0 \le u(t) \le 1$

$t_f = 10, \, E=1, \, c=17.5$

$r=0.71, \, k=80.5, \, U_{max}=20$
'''

from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

m = GEKKO(remote=False)

# time points 
n = 501
m.time = np.linspace(0,10,n)

e, c, r, k, u_max = 1, 17.5, 0.71, 80.5, 20

# rate 
u = m.MV(value=1, lb=0, ub=1)
u.STATUS = 1
u.DCOST = 0

# population
x = m.Var(70)

# population balance
m.Equation(x.dt() == r * x * (1 - x/k) - u*u_max)

# profit
j = m.Var(value=0) # objective
jF = m.FV() # final objective
jF.STATUS = 1

m.Connection(jF, j, pos2 = 'end')
m.Equation(j.dt() == (e - c / x) * u * u_max)

m.Obj(-j)

m.options.IMODE = 6 # optimal control mode
m.options.NODES = 3
m.options.SOLVER = 3

m.solve(disp=False)

print(jF.value[0])

plt.figure(1) # plot results
plt.subplot(2,1,1)
plt.plot(m.time,j.value,'r--',label='profit')
plt.plot(m.time,x.value,'b-',label='popul')
plt.legend()
plt.subplot(2,1,2)
plt.plot(m.time,u.value,'k--',label='rate')

plt.legend()
plt.show()
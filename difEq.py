'''
Solve the following differential equation with initial condition y(0)=5:

k * dy/dt= −ty
where k=10. The solution of y(t) should be reported from an initial time 0 
to final time 20. Create of plot of the result for y(t) versus t.
'''

from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

# numerical solution with gekko
m=GEKKO(remote=False)

m.time = np.linspace(0, 20, 100)
k = 10
y = m.Var(value=5)
t =  m.Param(value = m.time)
m.Equation(k * y.dt() == -t * y)

m.options.IMODE = 4 # dynamic simulation
m.options.NODES = 3
m.solve(disp=False)

# analytical solution:
ya = 5.0 * np.exp(-m.time**2/(2*k)) 

# solution with scipy
from scipy.integrate import odeint
def model(y, t):
    dydt = -t * y / k
    return dydt
yOdeint = odeint(model, 5, m.time)


plt.plot(m.time, y.value, 'b--', label='gekko')
plt.plot(m.time, ya, 'r--', label='analytic')
plt.plot(m.time, yOdeint, 'g:', label='ODEINT')
plt.legend()
plt.show()
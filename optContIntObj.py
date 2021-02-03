'''
Original Form

$\min_u \frac{1}{2} \int_0^2 x_1^2(t) \, dt$

$\mathrm{subject \; to}$

$\frac{dx_1}{dt}=u$

$x_1(0) = 1$

$-1 \le u(t) \le 1$

Equivalent Form for GEKKO with new Variable $x_2$

$\min_u x_2\left(t_f\right)$

$\mathrm{subject \; to}$

$\frac{dx_1}{dt}=u$

$\frac{dx_2}{dt} = \frac{1}{2} x_1^2(t)$

$x_1(0) = 1$

$x_2(0) = 0$

$t_f = 2$

$-1 \le u(t) \le 1$
'''

from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

m=GEKKO(remote=False)
nt = 101
m.time = np.linspace(0, 2, nt)
x1 = m.Var(value=1)
x2 = m.Var(value=0)
u = m.Var(value=0, lb=-1, ub=1)
p = np.zeros(nt)
p[-1] = 1
final = m.Param(value=p)

m.Equation(x1.dt() == u)
m.Equation(x2.dt() == .5 * x1**2)
m.Obj(x2 * final)

m.options.IMODE = 6 # optimal control mode, dynamic optimization
m.solve(disp=False)

plt.figure(1)
plt.plot(m.time,x1.value,'k-',label=r'$x_1$')
plt.plot(m.time,x2.value,'b-',label=r'$x_2$')
plt.plot(m.time,u.value,'r--',label=r'$u$')
plt.legend(loc='best')
plt.show()
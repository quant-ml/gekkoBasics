'''
Solve the following nonlinear optimization problem:

min x1x4(x1+x2+x3)+x3
s.t.x1x2x3x4≥25
x_1**2+x_2**2+x_3**2+x_4**2=40
1≤x1,x2,x3,x4≤5
with initial conditions:

x0=(1,5,5,1)
'''

from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

m=GEKKO(remote=False)

x1 = m.Var(value=1, lb=1, ub=5)
x2 = m.Var(value=5, lb=1, ub=5)
x3 = m.Var(value=5, lb=1, ub=5)
x4 = m.Var(value=1, lb=1, ub=5)

m.Equation(x1 * x2 * x3 * x4 >= 25)
m.Equation(x1**2 + x2**2 + x3**2 + x4**2 == 40)

m.Obj(x1 * x4 * (x1 + x2 + x3) + x3)

m.options.IMODE = 3
m.solve(disp=True)
print(x1.value[0], x2.value[0], x3.value[0], x4.value[0])
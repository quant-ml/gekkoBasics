from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

m=GEKKO(remote=False)

# measurements
xm = np.array([0,1,2,3,4,5])
ym = np.array([0.1,0.2,0.3,0.5,0.8,2.0])

# parameters
x = m.Param(value=xm)

a = m.FV()
a.STATUS = 1 # 0: fixed, 1: can be calculated

b = m.FV()
b.STATUS = 1

# vars

# option [1]:
y = m.CV(value=ym)
y.FSTATUS=1

# # option [2]:
# yp = m.Param(value = ym)
# y = m.Var()
# m.Obj(((yp - y) / yp) ** 2)

m.Equation(y == .1 * m.exp(a * x) + b) # regression equation

m.options.EV_TYPE = 2
m.options.IMODE = 2 # regr mode
m.solve(disp=False)

print(a.value[0], b.value[0])

plt.plot(xm,ym,'bo')
plt.plot(xm,y.value,'r-')
plt.show()
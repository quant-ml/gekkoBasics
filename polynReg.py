from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

m=GEKKO(remote=False)

xm = np.array([0,1,2,3,4,5])
ym = np.array([0.1,0.2,0.3,0.5,0.8,2.0])

m.options.IMODE=2

# coeffs:
c = [m.FV(value=0) for i in range(4)]
x = m.Param(value=xm)
y = m.CV(value=ym) # cv: match the model and the measured value
y.FSTATUS = 1 # we gonna use the measurements

# polynom model itself
m.Equation(y==c[0] + c[1] * x + c[2] * x ** 2 + c[3] * x ** 3)

# linReg 
c[0].STATUS = 1
c[1].STATUS = 1
m.options.EV_TYPE = 1 # error is absolute
# m.options.EV_TYPE = 2 # error is squarred

m.solve(disp=False)
p1 = [c[1].value[0], c[0].value[0]]
xp = np.linspace(0,5,100)

c[2].STATUS = 1
m.solve(disp=False)
p2 = [c[2].value[0], c[1].value[0], c[0].value[0]]

c[3].STATUS = 1
m.solve(disp=False)
p3 = [c[3].value[0], c[2].value[0], c[1].value[0], c[0].value[0]]

plt.plot(xm, ym, 'ko', label='data')
plt.plot(xp, np.polyval(p1,xp), 'b--', label='linear')
plt.plot(xp, np.polyval(p2,xp), 'r--', label='quad')
plt.plot(xp, np.polyval(p3,xp), 'g:', label='cub')
plt.legend(loc='best')
plt.show()


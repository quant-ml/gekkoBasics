'''
interpolation with cubic spline
'''

from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

m=GEKKO(remote=False)

xm = np.array([0,1,2,3,4,5])
ym = np.array([0.1,0.2,0.3,0.5,1.0,0.9])
x = m.Param(value=np.linspace(-1, 6))
y = m.Var()
m.cspline(x, y, xm, ym)
m.options.IMODE = 2
m.solve(disp=False)

# plt.plot(xm, ym, 'bo')
# plt.plot(x.value, y.value, 'r--', label='cubicSpline')
# plt.legend()
# plt.show()

# find extemum
p = GEKKO(remote=False)
p.x = p.Var(value=1, lb=0, ub=5)
p.y = p.Var()
p.Obj(-p.y)
p.cspline(p.x, p.y, xm, ym)
p.solve(disp=False)

plt.plot(xm, ym, 'bo', label='data')
plt.plot(x.value, y.value, 'r--', label='cubicSpline')
plt.plot(p.x, p.y, 'go', label='max')
plt.legend()
plt.show()
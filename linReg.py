'''
2: Solve Linear Equations
3x+2y=1
x+2y=0
'''
from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

m=GEKKO(remote=False)

x, y = m.Var(), m.Var()
# m.Equation(3 * x + 2 * y == 1)
# m.Equation(x + 2 * y == 0)
m.Equations([
    3 * x + 2 * y == 1, x + 2 * y == 0
])
m.solve(disp=False)
print(x.value[0], y.value[0])
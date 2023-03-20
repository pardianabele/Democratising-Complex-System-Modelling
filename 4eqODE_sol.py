import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def equations(t, y, z, p, q, f, g, d):
    # y[0] = x, y[1] = y, y[2] = a, y[3] = b
    dxdt = np.power(z, 1 / p) - y[0] * np.power(y[2], f)
    dydt = np.power(z, 1 / q) - y[1] * y[3] * np.power(y[2], g) - y[1] * np.power(y[2], d)
    dadt = - y[0] * np.power(y[2], f) - y[1] * y[3] * np.power(y[2], g) - y[1] * np.power(y[2], d)
    dbdt = y[0] * np.power(y[2], f) - y[1] * y[3] * np.power(y[2], g)

    return [dxdt, dydt, dadt, dbdt]

p = 2  # alpha
q = 1  # betha

f = 1
g = 3    # ! now g > d =>
d = 2

z = 1
init = [8, 10, 40, 0]  # x0, y0, a0, b0

# Time range to solve for
t_eval = np.linspace(0, 10, 10)

# Solve the ODEs
solution = solve_ivp(equations, (0, 10), init, args=(z, p, q, f, g, d), t_eval=t_eval, method='Radau')

# Plot the solutions
plt.plot(solution.t, solution.y[0], label='x')
plt.plot(solution.t, solution.y[1], label='y')
plt.plot(solution.t, solution.y[2], label='a')
plt.plot(solution.t, solution.y[3], label='b')
plt.xlabel('t')
plt.ylabel('concentration')
plt.legend()
plt.show()

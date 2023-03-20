import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def equations(t, y, z, a, p, q, f, g, d):
    # y[0] = x, y[1] = y, y[2] = b
    dxdt = np.power(z, 1 / p) - y[0] * np.power(a, f)
    dydt = np.power(z, 1 / q) - y[1] * y[2] * np.power(a, g) - y[1] * np.power(a, d)
    #dadt = - y[0] * np.power(y[2], f) - y[1] * y[3] * np.power(y[2], g) - y[1] * np.power(y[2], d)
    dbdt = y[0] * np.power(a, f) - y[1] * y[2] * np.power(a, g)

    return [dxdt, dydt, dbdt]

p = 2  # alpha
q = 1  # betha

f = 1
g = 3
d = 2

z = 2
a = 100
init = [10, 15, 0]  # x0, y0, b0

# Time range to solve for
t_eval = np.linspace(0, 10, 5)

# Solve the ODEs
solution = solve_ivp(equations, (0, 10), init, args=(z, a, p, q, f, g, d), t_eval=t_eval, method='Radau')

print(solution.y[0])
print("--------------------------")
print(solution.y[2])

# Plot the solutions
plt.plot(solution.t, solution.y[0], label='x')
plt.plot(solution.t, solution.y[1], label='y')
plt.plot(solution.t, solution.y[2], label='b')

plt.xlabel('time (s)')
plt.ylabel('concentration')
plt.legend()
plt.show()

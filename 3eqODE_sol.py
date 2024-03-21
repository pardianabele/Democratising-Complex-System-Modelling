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

p = 1  # alpha
q = 2  # betha

f = 3
g = 2
d = 1

z = 1
a = 10
init = [0.3, 0.6, 0]  # x0, y0, b0

# Time range to solve for
t_eval = np.linspace(0, 3, 3)

# Solve the ODEs
solution = solve_ivp(equations, (0, 3), init, args=(z, a, p, q, f, g, d), t_eval=t_eval, method='Radau')

print(solution.y[0])
print("--------------------------")
print(solution.y[2])

# Plot the solutions
plt.plot(solution.t, solution.y[0], label='x')
plt.plot(solution.t, solution.y[1], label='y')
plt.plot(solution.t, solution.y[2], label='b')

plt.xlabel('Time steps')
plt.ylabel('Concentration (unitless)')
plt.legend()
plt.show()

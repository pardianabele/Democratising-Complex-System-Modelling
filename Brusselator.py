import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def equations(t, y, a, b):
    # y[0] = x, y[1] = y
    dxdt = a - (b + 1) * y[0] + np.power(y[0], 2) * y[1]
    dydt = b * y[0] - np.power(y[0], 2) * y[1]

    return [dxdt, dydt]


a = 100
b = 100
init = [0, 0]  # x0, y0

# Time range to solve for
t_eval = np.linspace(0, 1, 1000)

# Solve the ODEs
solution = solve_ivp(equations, (0, 300), init, args=(a, b), t_eval=t_eval, method='Radau')

print(solution.y[0])
print("--------------------------")
print(solution.y[1])

# Plot the solutions
plt.plot(solution.t, solution.y[0], label='x', linewidth=3)
plt.plot(solution.t, solution.y[1], label='y', linewidth=3)

plt.xlabel('Time steps')
plt.ylabel('Concentration (unitless)')
plt.legend()
plt.show()

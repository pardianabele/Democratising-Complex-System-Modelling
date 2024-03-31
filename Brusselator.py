import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def equations(t, y, a, b):
    dxdt = a - (b + 1) * y[0] + np.power(y[0], 2) * y[1]
    dydt = b * y[0] - np.power(y[0], 2) * y[1]
    return [dxdt, dydt]

a = 1.5
b = 3
init = [1, 1]


t_span = (0, 10)
t_eval = np.linspace(0, 10, 500)

solution = solve_ivp(equations, t_span, init, args=(a, b), t_eval=t_eval, method='Radau')

plt.figure(figsize=(10, 5))
plt.plot(solution.t, solution.y[0], label='x', linewidth=2)
plt.plot(solution.t, solution.y[1], label='y', linewidth=2)

plt.xlabel('Time steps')
plt.ylabel('Concentration (unitless)')

plt.legend()
plt.grid(True)
plt.show()

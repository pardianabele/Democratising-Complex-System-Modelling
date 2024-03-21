import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

'''
def equations(t, y, z, p, q, f, g, d):
    # y[0] = x, y[1] = y, y[2] = a, y[3] = b
    dxdt = np.power(z, 1 / p) - y[0] * np.power(y[2], f)
    dydt = np.power(z, 1 / q) - y[1] * y[3] * np.power(y[2], g) - y[1] * np.power(y[2], d)
    dadt = - y[0] * np.power(y[2], f) - y[1] * y[3] * np.power(y[2], g) - y[1] * np.power(y[2], d)
    dbdt = y[0] * np.power(y[2], f) - y[1] * y[3] * np.power(y[2], g)

    return [dxdt, dydt, dadt, dbdt]
'''

def func_ss(s, p, q, f, g, d):
    x, y, a, b = s
    return (np.power(t, 1 / p) - x * np.power(a, f),
            np.power(t, 1 / q) - y * b * np.power(a, g) - y * np.power(a, d),
            -x * np.power(a, f) - y * b * np.power(a, g) - y * np.power(a, d),
            x * np.power(a, f) - y * b * np.power(a, g))

initial_guess = (20, 20, 0, 0)

p = 3  # alpha
q = 1  # betha

f = 1
g = 2    # ! now g > d =>
d = 1

t = 100

solution = fsolve(func_ss, initial_guess, args=(p, q, f, g, d))
print(solution)

'''
init = [0.3, 0.6, 6, 0]  # x0, y0, a0, b0

# Time range to solve for
t_eval = np.linspace(0, 2, 2)

# Solve the ODEs
solution = solve_ivp(equations, (0, 5), init, args=(z, p, q, f, g, d), t_eval=t_eval, method='Radau')

# Plot the solutions
plt.plot(solution.t, solution.y[0], label='x')
plt.plot(solution.t, solution.y[1], label='y')
plt.plot(solution.t, solution.y[2], label='a')
plt.plot(solution.t, solution.y[3], label='b')
plt.xlabel('Time steps')
plt.ylabel('Concentration (unitless)')
plt.legend()
plt.show()
'''


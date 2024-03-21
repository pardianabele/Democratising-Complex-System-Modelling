import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

p = 2
q = 1

f = 3
g = 2
d = 1

t = 100
a = 100

def initial_values(t, p, q):
    k = 1
    x = k*np.power(t, 1/p)
    y = k*np.power(t, 1/q)
    return x, y

def equations(s):
    x, y, b = s
    return (np.power(t, 1 / p) - x * np.power(a, f),
            np.power(t, 1 / q) - y * b * np.power(a, g) - y * np.power(a, d),
            x * np.power(a, f) - y * b * np.power(a, g))

initial_guess = (0, 0, 0)
solution = fsolve(equations, initial_guess)
print(solution)

# Your system of ODEs
def F(t, y):
    x, y, b = y

    dxdt = np.power(t, 1 / p) - x * np.power(a, f)
    dydt = np.power(t, 1 / q) - y * b * np.power(a, g) - y * np.power(a, d)
    dbdt = x * np.power(a, f) - y * b * np.power(a, g)

    return [dxdt, dydt, dbdt]

# Initial conditions
x_limit, y_limit = initial_values(t, p, q)
y0 = [x_limit, y_limit, 0]
t = [0, 10]  # Time range

# Solve the system of equations
sol = solve_ivp(F, t, y0, dense_output=True)

# Get the solutions
t = np.linspace(0, 10, 10)  # You can adjust the number of points as needed
y = sol.sol(t)

# Plot the phase space trajectory in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(solution[0], solution[1], solution[2], c='r', marker='o', s=25, zorder=20)
ax.plot(y[0], y[1], y[2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('b')
plt.show()

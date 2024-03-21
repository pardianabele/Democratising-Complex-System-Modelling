import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

p = 2
q = 1
f = 3
g = 2
d = 1
t = 100  # t = 1000000

# Define the symbols
x, y, z, a = sp.symbols('x y z a')

# Define the equations
eq1 = sp.Eq(sp.Pow(t, 1 / p) - x * sp.Pow(a, f), 0)
eq2 = sp.Eq(sp.Pow(t, 1 / q) - y * z * sp.Pow(a, g) - y * sp.Pow(a, d), 0)
eq3 = sp.Eq(x * sp.Pow(a, f) - y * z * sp.Pow(a, g), 0)

# Solve the system of equations
steady_state_sol = sp.solve((eq1, eq2, eq3), (x, y, z))
print("Steady state solution: ", steady_state_sol)

# Define the parameter range
a_values = np.linspace(1, 100, 1000)  # start from 1 to avoid division by zero

# Define the steady state solutions
x_sol_function = sp.lambdify(a, steady_state_sol[0][0], 'numpy')
y_sol_function = sp.lambdify(a, steady_state_sol[0][1], 'numpy')
z_sol_function = sp.lambdify(a, steady_state_sol[0][2], 'numpy')

print("x_sol_function: ", x_sol_function)
print("y_sol_function: ", y_sol_function)
print("z_sol_function: ", z_sol_function)

x_sol = x_sol_function(a_values)
y_sol = y_sol_function(a_values)
z_sol = z_sol_function(a_values)

print("x_sol: ", x_sol)
print("y_sol: ", y_sol)
print("z_sol: ", z_sol)

# Create a new figure
fig = plt.figure()

# Create a 3D plot
ax = fig.add_subplot(111, projection='3d')
ax.plot(a_values, x_sol, y_sol, z_sol)

# Set labels
ax.set_xlabel('a')
ax.set_ylabel('X_ss')
ax.set_zlabel('Y_ss')

# Show the plot
plt.show()

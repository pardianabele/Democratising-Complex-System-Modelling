import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import fsolve

# Coefficients and initial conditions
p = 2  # alpha
q = 1  # betha
f = 3
g = 2  # when g > d, gA is smaller than dA
d = 1
t = 2 # this is z0 in our case but because z is reserved I had to rename the variable
a = 100

def equations(s):
    x, y, b = s
    return (np.power(t, 1 / p) - x * np.power(a, f),
            np.power(t, 1 / q) - y * b * np.power(a, g) - y * np.power(a, d),
            x * np.power(a, f) - y * b * np.power(a, g))

initial_guess = (0, 0, 0)
solution = fsolve(equations, initial_guess)
print(solution)

# Define the saddle point function
def saddle_point(x, y, z):
    return (np.power(t, 1 / p) - x * np.power(a, f)) * (np.power(t, 1 / q) - y * z * np.power(a, g) - y * np.power(a, d)) * (x * np.power(a, f) - y * z * np.power(a, g))

# Generate grid for 3D plot
x = np.linspace(-200, 200, 500)
y = np.linspace(-200, 200, 500)
X, Y = np.meshgrid(x, y)
Z = saddle_point(X, Y, 0)  # z = 0

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the saddle point function
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Add a color bar
fig.colorbar(surf)

# Add labels and a title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y, z=0)')
title = "Saddle Point Function"
ax.set_title(f"{title}\n for (\u03b1, \u03b2, f, g, d): {p, q, f, g, d}")

# Show the plot
plt.show()

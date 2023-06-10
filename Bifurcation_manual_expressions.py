import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

p = 3
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
a = np.linspace(10, 500, 10000)  # avoid division by zero

# Define the steady state solutions

#
x_ss = 4.64158883361278 / np.power(a, 3)
y_ss = 95.3584111663872 / a
z_ss = 0.0486751905452142 / a

# Create a new figure
fig = plt.figure()

# Create a 3D plot
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(x_ss, y_ss, z_ss, c=a, cmap=plt.get_cmap('plasma'))

fig.colorbar(sc, label='a')
# Set labels
ax.set_xlabel('X_ss')
ax.set_ylabel('Y_ss')
ax.set_zlabel('Z_ss')

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

p = 1
q = 3

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
a = np.linspace(4, 200, 10000)  # avoid division by zero

# Define the steady state solutions

# 13321
x_6 = 100/ np.power(a, 3)
y_6 = -95.358 / a
z_6 = -1.048 / a

# 23321
x_5 = 100/ np.power(a, 3)
y_5 = -5.358 / a
z_5 = -1.866 / a

# 12321
x_4 = 100/ np.power(a, 3)
y_4 = -90 / a
z_4 = -1.11 / a

# 32321
x_3 = 4.64158883361278 / np.power(a, 3)
y_3 = 5.35841116638722 / a
z_3 = 0.866224835960518 / a

# 21321
x_2 = 10 / np.power(a, 3)
y_2 = 90 / a
z_2 = 0.111111111111111 / a

# 31321
x_1 = 4.64158883361278 / np.power(a, 3)
y_1 = 95.3584111663872 / a
z_1 = 0.0486751905452142 / a

# Create a new figure
fig = plt.figure()

# Create a 3D plot

ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(x_1, y_1, z_1, c=a, cmap=plt.get_cmap('plasma'))
ax.text(x_1[0], y_1[0], z_1[0], '(3,1)', color='black', weight='bold')
sc = ax.scatter(x_2, y_2, z_2, c=a, cmap=plt.get_cmap('plasma'))
ax.text(x_2[0], y_2[0], z_2[0], '(2,1)', color='black', weight='bold')
sc = ax.scatter(x_3, y_3, z_3, c=a, cmap=plt.get_cmap('plasma'))
ax.text(x_3[0], y_3[0], z_3[0], '(3,2)', color='black', weight='bold')
'''
sc = ax.scatter(x_4, y_4, z_4, c=a, cmap=plt.get_cmap('plasma'))
ax.text(x_4[0], y_4[0], z_4[0], '(1,2)', color='black', weight='bold')
sc = ax.scatter(x_5, y_5, z_5, c=a, cmap=plt.get_cmap('plasma'))
ax.text(x_5[0], y_5[0], z_5[0], '(2,3)', color='black', weight='bold')
sc = ax.scatter(x_6, y_6, z_6, c=a, cmap=plt.get_cmap('plasma'))
ax.text(x_6[0], y_6[0], z_6[0]-0.1, '(1,3)', color='black', weight='bold')
'''

fig.colorbar(sc, label='a', pad=0.12)

ax.set_xticks([0, 0.02, 0.05, 0.07, 0.1, 0.12, 0.15])

ax.set_xlabel('x_ss')
ax.set_ylabel('y_ss')
ax.set_zlabel('b_ss')

# Show the plot
plt.show()



from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata


p = 2
q = 1

f = 3
g = 2
d = 1

t = 100 #t = 1000000
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

def saddle_point(x, y, z):
    return (np.power(t, 1 / p) - x * np.power(a, f)) * (
            np.power(t, 1 / q) - y * z * np.power(a, g) - y * np.power(a, d)) * (
            x * np.power(a, f) - y * z * np.power(a, g))


spacing = 40

x_limit, y_limit = initial_values(t, p, q)
print(x_limit, y_limit)

def projection(x, y, z):
    #y is b
    #z is a
    return (np.power(t, 1 / p) - x * np.power(z, f)) * (
            np.power(t, 1 / q) - y_limit * y * np.power(z, g) - y_limit * np.power(z, d)) * (
            x * np.power(z, f) - y_limit * y * np.power(z, g))


#x = np.linspace(-500, 500, spacing)
#y = np.linspace(-500, 500, spacing)
#z = np.linspace(-500, 500, spacing)

x = np.linspace(0, x_limit, spacing)
y = np.linspace(0, y_limit, spacing)
z = np.linspace(0, x_limit, spacing)


xs = []
ys = []
zs = []
vals = []
minVal = 1000
maxVal = 0

for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(z)):
            val = saddle_point(x[i], y[j], z[k]) / 1e24
            #if x[i] < 0 or y[j] < 0 or z[k] < 0:
            #    continue
            #if val < -0.0001: #> 0.06 or val < 0.05:
            #    continue
            if val < minVal:
                minVal = val
            if val > maxVal:
                maxVal = val
            xs.append(x[i])
            ys.append(y[j])
            zs.append(z[k])
            vals.append(val)

print("minVal", minVal)
print("maxVal", maxVal)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(xs, ys, zs, c=vals, cmap="plasma", vmin=minVal, vmax=maxVal, s=5)
ax.scatter(solution[0], solution[1], solution[2], c='r', marker='o', s=25, zorder=20)
# Create the color bar with a padding of 0.05 (adjust as needed)
cbar = plt.colorbar(sc, pad=0.09)

# Add a label to the color bar
cbar.set_label('1e24')

# Adjust the position of the color bar using the set_ticks_position() method
#cbar.ax.yaxis.set_ticks_position('left')
ax.set_xlim(0, x_limit)  # Set x-axis limits from 0 to 6
ax.set_ylim(0, y_limit)  # Set y-axis limits from 0 to 12
ax.set_zlim(0, x_limit)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('b')

title = "Saddle Function"
ax.set_title(f"{title}\n for (\u03b1, \u03b2, f, g, d, a): {p, q, f, g, d, a}")

plt.show()

#---------------------- bifurcation analysis --------------

def plot_2d_slice(xs, ys, zs, vals, y_value):
    # Get the 2D slice for the specified y value
    slice_xs, slice_zs, slice_vals = [], [], []

    for x, y, z, val in zip(xs, ys, zs, vals):
        if y == y_value:
            slice_xs.append(x)
            slice_zs.append(z)
            slice_vals.append(val)

    return slice_xs, slice_zs, slice_vals

xs, zs, vals = plot_2d_slice(xs, ys, zs, vals, y_value=y_limit)

td = plt.scatter(xs, zs, c=vals, cmap="plasma", vmin=minVal, vmax=maxVal, s=5)
cbar = plt.colorbar(td, pad=0.09)

cbar.set_label('1e24')

plt.xlabel('x')
plt.ylabel('b')

title = "Slice of saddle function"
plt.title(f"{title}\n at (\u03b1, \u03b2, f, g, d, y, a): {p, q, f, g, d, y_limit, a}")

plt.show()

#------------------------------- contour plot at y lim ------------------------
# Define the grid
xi = np.linspace(min(xs), max(xs), 100)
zi = np.linspace(min(zs), max(zs), 100)
xi, zi = np.meshgrid(xi, zi)

# Interpolate values onto the grid
interpolated_vals = griddata((xs, zs), vals, (xi, zi), method='cubic')

# Create the contour plot
tdl = plt.contourf(xi, zi, interpolated_vals, levels=10, cmap="plasma", vmin=minVal, vmax=maxVal)

cbar = plt.colorbar(tdl, pad=0.09)

cbar.set_label('1e24')

plt.xlabel('x')
plt.ylabel('b')

title = "Slice of saddle function"
plt.title(f"{title}\n at (\u03b1, \u03b2, f, g, d, y, a): {p, q, f, g, d, int(y_limit), a}")

plt.show()

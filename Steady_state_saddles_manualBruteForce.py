from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np


p = 2
q = 1

f = 1
g = 2
d = 1

t = 100 #t = 1000000
a = 3

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
#print("values", vals)

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

title = "Saddle Point Function"
ax.set_title(f"{title}\n for (\u03b1, \u03b2, f, g, d, a): {p, q, f, g, d, a}")

plt.show()

#---------------------- analysis --------------

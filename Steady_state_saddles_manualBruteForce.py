import matplotlib.pyplot as plt
import numpy as np

p = 2
q = 1
f = 3
g = 2
d = 1
t = 2
a = 100


def saddle_point(x, y, z):
    return (np.power(t, 1 / p) - x * np.power(a, f)) * (
            np.power(t, 1 / q) - y * z * np.power(a, g) - y * np.power(a, d)) * (
            x * np.power(a, f) - y * z * np.power(a, g))


spacing = 50

x = np.linspace(-200, 200, spacing)
y = np.linspace(-200, 200, spacing)
z = np.linspace(-200, 200, spacing)

xs = []
ys = []
zs = []
vals = []
minVal = 1000
maxVal = 0

for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(z)):
            val = saddle_point(x[i], y[j], z[k]) / 1e25
            if x[i] < 0 or y[j] < 0 or z[k] < 0:
                continue
            if val < minVal:
                minVal = val
            if val > maxVal:
                maxVal = val
            xs.append(x[i])
            ys.append(y[j])
            zs.append(z[k])
            vals.append(val)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(xs, ys, zs, c=vals, cmap="viridis", vmin=minVal, vmax=maxVal, s=5)
plt.colorbar(sc)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

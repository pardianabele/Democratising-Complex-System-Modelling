from scipy.optimize import fsolve
# import matplotlib.pyplot as plt
import numpy as np
from mayavi import mlab

# Coefficients and initial conditions

p = 2  # alpha
q = 1  # betha

f = 3
g = 2  #!! when g > d, gA is smaller than dA
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


X, Y, Z = np.mgrid[-200:200:500j, -200:200:500j, -200:200:500j]

W = saddle_point(X, Y, Z)

fig = mlab.figure()

src = mlab.pipeline.scalar_field(X, Y, Z, W)
iso_surface = mlab.pipeline.iso_surface(src, contours=[0], opacity=1, colormap='viridis')

mlab.axes(xlabel='x', ylabel='y', zlabel='b')

color_bar = mlab.scalarbar(iso_surface, title='Saddle Point Value', orientation='vertical', nb_labels=5)
color_bar.scalar_bar_representation.position = [0.8, 0.2]
color_bar.scalar_bar_representation.position2 = [0.05, 0.6]

# Set the scalar range for the color bar
#iso_surface.module_manager.scalar_lut_manager.range = np.array([10**-24, 10**24])

# Set the title using mlab.title()
title = "Saddle Point Function"
full_title = f"{title}\n for (\u03b1, \u03b2, f, g, d): {p, q, f, g, d}"
mlab.title(full_title, size=0.4)  # Adjust the size parameter to change the font size

mlab.show()
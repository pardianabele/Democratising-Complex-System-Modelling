from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

# Coefficients and initial conditions

p = 3  # alpha
q = 2  # betha

f = 2
g = 3  #!! when g > d, gA is smaller than dA
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

# Create a meshgrid of x and y values
# for full saddles:
x = np.linspace(-200, 200, 500)
y = np.linspace(-200, 200, 500)
z = np.linspace(-200, 200, 500)

#for the positive spectrum of the saddles
#x = np.linspace(0.00000125, 20, 50) #  (0.001, 40, 50) for 21221
#y = np.linspace(0.0015, 5, 50)
#z = np.linspace(0.005, 5, 50)  #(0, 10, 50)

X, Y = np.meshgrid(x, y)

# Compute the saddle point function
W = saddle_point(X, Y, z)

# Mask the negative values of x, y, and z
X_pos = np.ma.masked_where(X < 0, X)
Y_pos = np.ma.masked_where(Y < 0, Y)
W_pos = np.ma.masked_where(W < 0, W)

#print(X_pos)
#print(Y_pos)
#for i in range(0, 50):
#    print(i, W_pos[i])


#contour_levels = np.linspace(np.min(W), np.max(W), 10)

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the saddle point function
surface = ax.plot_surface(X, Y, W, cmap='viridis', alpha=1)  # for full saddle
#surface = ax.plot_surface(X_pos, Y_pos, W_pos, cmap='viridis', alpha=1)  # for the positive spectrum of the saddle

fig.colorbar(surface, pad=0.15)

#ax.contour(X_pos, Y_pos, W_pos, contour_levels, colors='k')

#contours = ax.contour(X, Y, W, levels=[0], colors='red')
#ax.clabel(contours, inline=True, fontsize=10)

ax.scatter(solution[0], solution[1], solution[2], c='r', marker='o', s=25, zorder=20)

# Set the axis limits
# ax.set_xlim(0.0000000001, 2)
#ax.set_ylim(-10, 10)
#ax.set_zlim(0, 100000000)

# Add labels and a title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('b')

title = "Saddle Point Function"
ax.set_title(f"{title}\n for (\u03b1, \u03b2, f, g, d): {p, q, f, g, d}")

# Show the plot
plt.show()




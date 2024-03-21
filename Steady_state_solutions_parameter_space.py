from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

# Initial conditions

t = 2 # this is z0 in our case but because z is reserved I had to rename the variable
a = 100

def equations(s, p, q, f, g, d):
    x, y, b = s
    return (np.power(t, 1 / p) - x * np.power(a, f),
            np.power(t, 1 / q) - y * b * np.power(a, g) - y * np.power(a, d),
            x * np.power(a, f) - y * b * np.power(a, g))

initial_guess = (0, 0, 0)

# arrays to work with when plotting

pp = []  # alpha
qq = []  # betha

ff = []
gg = []
dd = []
xx = []
yy = []
bb = []

parameter_space = [1, 2, 3]

for p in parameter_space:
    for q in parameter_space:
        for f in parameter_space:
            for g in parameter_space:
                for d in parameter_space:
                    if p > q and d < g:
                        solution = fsolve(equations, initial_guess, args=(p, q, f, g, d))
                        if solution[0] > 0 and solution[1] > 0 and solution[2] > 0:
                            pp.append(p)
                            qq.append(q)
                            ff.append(f)
                            gg.append(g)
                            dd.append(d)
                            xx.append(solution[0])
                            yy.append(solution[1])
                            bb.append(solution[2])
                            print(p, q, f, g, d, solution[0], solution[1], solution[2])
                        else:
                            print(p, q, f, g, d, solution[0], solution[1], solution[2])
                            print("-------WARNING------------")

print(len(pp), len(xx))

b_log = np.log10(bb)
x_log = np.log10(xx)
y_log = np.log10(yy)
# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(x_log, y_log, b_log, c='black', marker='o', s=5, alpha=0.7)

# mark the key points with different colours

# (2 1 1 2 1) 0.014142135623730952 0.005857864376269048 0.02414213562373104
# (2 1 1 3 1) 0.014142135623730952 0.005857864376269049 0.00024142135623730953
# (2 1 1 3 2) 0.01414213562373095 5.857864376269049e-05 0.024142135623730975
# (2 1 2 2 1) 0.0001414213562373095 0.005857864376269049 0.02414213562373091
# (3 1 1 2 1) 0.01259921049894873 0.007400789501051269 0.017024143839193137
# (3 2 1 2 1) 0.012599210498948733 0.0015429251247822194 0.0816579514882625

# (2 1 3 2 1) 1.4142135623730952e-06 0.005857864376269049 0.02414213562373089
# (3 2 3 2 1) 1.2599210498948732e-06 0.0015429251247822196 0.0816579514882637
# (3 1 3 2 1) 1.2599210498948732e-06 0.007400789501051268 0.017024143839193144

# 3 2 3 3 2 1.2599210498948732e-06 1.5429251247822197e-05 0.08165795148826341


ax.scatter(np.log10(0.014142135623730952), np.log10(0.005857864376269048), np.log10(0.02414213562373104), c='red', marker='x', s=50)
ax.scatter(np.log10(0.014142135623730952), np.log10(0.005857864376269049), np.log10(0.00024142135623730953), c='cyan', marker='x', s=50)
ax.scatter(np.log10(0.01414213562373095), np.log10(5.857864376269049e-05), np.log10(0.024142135623730975), c='blue', marker='x', s=50)
ax.scatter(np.log10(0.0001414213562373095), np.log10(0.005857864376269049), np.log10(0.02414213562373091), c='green', marker='x', s=50)
ax.scatter(np.log10(0.01259921049894873), np.log10(0.007400789501051269), np.log10(0.017024143839193137), c='brown', marker='x', s=50)
ax.scatter(np.log10(0.012599210498948733), np.log10(0.0015429251247822194), np.log10(0.0816579514882625), c='orange', marker='x', s=50)

ax.scatter(np.log10(1.4142135623730952e-06), np.log10(0.005857864376269049), np.log10(0.02414213562373089), c='magenta', marker='x', s=50)
ax.scatter(np.log10(1.2599210498948732e-06), np.log10(0.0015429251247822196), np.log10(0.0816579514882637), c='magenta', marker='x', s=50)
ax.scatter(np.log10(1.2599210498948732e-06), np.log10(0.007400789501051268), np.log10(0.017024143839193144), c='magenta', marker='x', s=50)

#ax.scatter(np.log10(1.2599210498948732e-06), np.log10(1.5429251247822197e-05), np.log10(0.08165795148826341), c='magenta', marker='x', s=50)

# Set the b-axis to be logarithmic
# Set the z-axis label and limits
ax.set_zlabel('10^z')
ax.set_xlabel('10^x')
ax.set_ylabel('10^y')
ax.set_zlim(-4, 1)#(-1, 2) #(-4, 1)
ax.set_xlim(-7, -1) #(-7, -1)
ax.set_ylim(-5, -2)#(-7, -2) #

# Modify the z-axis tick labels to display as 10^x
zticks = np.arange(-4, 2)
xticks = np.arange(-7, -1)[0::2]
yticks = np.arange(-5, -2)

ax.set_zticks(zticks)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_zticklabels([r'$10^{'+ str(x) + '}$' for x in zticks])
ax.set_xticklabels([r'$10^{'+ str(x) + '}$' for x in xticks])
ax.set_yticklabels([r'$10^{'+ str(x) + '}$' for x in yticks])
# Set the z-axis limits to ensure the data is not too compressed
#ax.set_zlim(bottom=<min_value>, top=<max_value>)

# Plot the saddle point function
#contour = ax.contourf(X, Y, W)
#surface = ax.plot_surface(X, Y, W, cmap='viridis', alpha=0.5) #0.3

#fig.colorbar(surface, pad=0.15)

#ax.scatter(solution[0], solution[1], solution[2], c='r', marker='o', s=25, zorder=20)

# Set the axis limits
#ax.set_xlim(-2, 2)
#ax.set_ylim(-10, 10)
#ax.set_zlim(-10, 0)

# Add labels and a title
ax.set_xlabel('x$_{sol}$')
ax.set_ylabel('y$_{sol}$')
ax.set_zlabel('b$_{sol}$')

#title = "Saddle Point Function"
#ax.set_title(f"{title}\n for (\u03b1, \u03b2, f, g, d): {p, q, f, g, d}")

# Show the plot
plt.show()




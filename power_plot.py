import numpy as np
import matplotlib.pyplot as plt

# Define the time interval
t = np.linspace(0, 7, 100)

# Define the parameters for the first equation x(t) = x0 * exp(-k*t)
x0 = 10
k = 0.5

# Compute the values of x(t)
x = x0 * np.exp(-k*t)

# Define the parameters for the second equation 1/y(t) = 1/y0 + k*t
y0 = 10

# Compute the values of y(t)
y = 1 / (k*t + 1/y0)

# Define the parameters for the third equation z(t) = z0/sqrt(2ktz0^2+1)
z0 = 10

# Compute the values of z(t)
z = z0 / np.sqrt(2*k*t*z0**2 + 1)

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the curves
ax.plot(t, x, label='First order reaction')
ax.plot(t, y, label='Second order reaction')
ax.plot(t, z, label='Third order reaction')

# Add a title, axis labels, and legend
#ax.set_title("k=0.2")
ax.set_xlabel("Time steps")
ax.set_ylabel("Concentration of A")
ax.legend()

# Show the plot
plt.show()

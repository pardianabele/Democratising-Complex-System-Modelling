import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from scipy.optimize import fsolve

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


X, Y, Z = np.mgrid[-200:200:100j, -200:200:100j, -200:200:100j]
W = saddle_point(X, Y, Z)

fig = go.Figure()

fig.add_trace(
    go.Isosurface(
        x=X.ravel(),
        y=Y.ravel(),
        z=Z.ravel(),
        value=W.ravel(),
        isomin=0,
        isomax=0,
        surface_count=1,
        opacity=1,
        colorscale='Viridis'
        #cmin=10**-4,
        #cmax=10**22,
    )
)

fig.update_layout(
    scene=dict(
        xaxis_title="x",
        yaxis_title="y",
        zaxis_title="b",
        xaxis=dict(showgrid=False),  # Add this line
        yaxis=dict(showgrid=False),  # Add this line
        zaxis=dict(showgrid=False),  # Add this line
    ),
    title=dict(
        text=f"Saddle Point Function<br>for (α, β, f, g, d): {p, q, f, g, d}",
        y=0.95,
        x=0.5,
        xanchor='center',
        yanchor='top',
    ),
    coloraxis_colorbar=dict(
        title="Saddle Point Value",
        tickmode="array"
        #tickvals=[10**i for i in range(-24, 25, 12)],
    ),
)

# Save the plot as a static image file
#pio.show(fig)
pio.write_image(fig, 'saddle_point_plot.png')
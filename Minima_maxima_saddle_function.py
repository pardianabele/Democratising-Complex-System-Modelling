from scipy.optimize import minimize
from scipy.optimize import differential_evolution
import numpy as np

p = 2
q = 1

f = 1
g = 2
d = 1

t = 2
a = 100


def saddle_function(x):
    return (np.power(t, 1 / p) - x[0] * np.power(a, f)) \
           * (np.power(t, 1 / q) - x[1] * x[2] * np.power(a, g) - x[1] * np.power(a, d)) \
           * (x[0] * np.power(a, f) - x[1] * x[2] * np.power(a, g))

# Find the maximum by minimizing the negation of the function
def negated_saddle_function(x):
    return -saddle_function(x)

# Bounds for x[0] (which represents x), x[1] (which represents y), and x[2] (which represents z)
bounds = [(0, 10), (0, 10), (0, 10)]

# Initial guess
x0 = [0, 0, 0]
print("Initial guess: ", x0)

# Find the minimum
result_min = minimize(saddle_function, x0, bounds=bounds)
print("Minimum:", result_min.fun, "at", result_min.x)

result_max = minimize(negated_saddle_function, x0, bounds=bounds)
print("Maximum:", -result_max.fun, "at", result_max.x)

result_min_global = differential_evolution(saddle_function, bounds)
print("Global minimum:", result_min_global.fun, "at", result_min_global.x)

result_max_global = differential_evolution(negated_saddle_function, bounds)
print("Global maximum:", -result_max_global.fun, "at", result_max_global.x)
import numpy as np
from scipy.optimize import minimize, minimize_scalar, fminbound
from scipy.linalg import eigvals

# Coefficients and initial conditions

p = 3  # alpha
q = 2  # betha

f = 2
g = 3  #!! when g > d, gA is smaller than dA
d = 1

t = 2 # this is z0 in our case but because z is reserved I had to rename the variable
a = 100


def function(x):
    return (np.power(t, 1 / p) - x[0] * np.power(a, f)) \
        * (np.power(t, 1 / q) - x[1] * x[2] * np.power(a, g) - x[1] * np.power(a, d))\
        * (x[0] * np.power(a, f) - x[1] * x[2] * np.power(a, g))

# Define constraints and bounds
constraints = {"type": "ineq", "fun": lambda x: x}
bounds = [(0, None), (0, None), (0, None)]


# Define initial guess
initial_guess = np.array([0, 0, 0])


# Find local minimum
min_result = minimize(function, initial_guess, constraints=constraints, bounds=bounds)
print("Local Minimum: ", min_result)

# Find local maximum by minimizing the negation of the function
negated_function = lambda x: -function(x)
max_result = minimize(negated_function, initial_guess, constraints=constraints, bounds=bounds)
print("Local Maximum: ", max_result)

print("#-------------- Grad and Hess --------------")
def gradient(x):
    return np.array([-np.power(a, f) * (np.power(a, f) * x[0] - np.power(a, g) * x[2] * x[1]) *
                     (-np.power(a, d) * x[1] - np.power(a, g) * x[1] * x[2] + np.power(t, 1 / q)) +
                     np.power(a, f) * (-np.power(a, f) * x[0] + np.power(t, 1 / p)) *
                     (-np.power(a, d) * x[1] - np.power(a, g) * x[1] * x[2] + np.power(t, 1 / q)),
                     (-np.power(a, d) - np.power(a, g) * x[2]) *
                     (np.power(a, f)* x[0] - np.power(a, g) * x[1] * x[2]) *
                     (-np.power(a, f) * x[0] + np.power(t, 1 / p)) -
                     np.power(a, g) * x[2] * (-np.power(a, f) * x[0] + np.power(t, 1 / p)) *
                     (-np.power(a, d) * x[1] - np.power(a, g) * x[1] * x[2] + np.power(t, 1 / q)),
                     -np.power(a, g) * x[1] * (np.power(a, f)* x[0] - np.power(a, g) * x[1] * x[2]) *
                    (-np.power(a, f)* x[0] + np.power(t, 1 / p)) -
                     np.power(a, g) * x[1] * (-np.power(a, f) * x[0] + np.power(t, 1 / p)) *
                    (-np.power(a, d) * x[1] - np.power(a, g) * x[1] * x[2] + np.power(t, 1 / q))])


def hessian(x):

    H11 = -2 * np.power(a, 2 * f) * (-np.power(a, d) * x[1] - np.power(a, g) * x[1] * x[2] + np.power(t, 1 / q))

    H12 = -np.power(a, f) * (-np.power(a, d) - np.power(a, g) * x[2]) * (np.power(a, f) * x[0] - np.power(a, g) * x[1] * x[2])
    + np.power(a, f) * (-np.power(a, d) - np.power(a, g) * x[2]) * (-np.power(a, f) * x[0] + np.power(t, 1 / p)) \
    + np.power(a, f + g) * x[2] * (-np.power(a, d) * x[1] - np.power(a, g) * x[1] * x[2] + np.power(t, 1 / q))

    H13 = np.power(a, f + g) * x[1] * (np.power(a, f) * x[0] - np.power(a, g) * x[1] * x[2]) - np.power(a, f + g) * x[1] \
          * (-np.power(a, f) * x[0] + np.power(t, 1 / p)) + np.power(a, f + g) * x[1] * (-np.power(a, d) * x[1]
          - np.power(a, g) * x[1] * x[2] + np.power(t, 1 / q))

    H21 = -np.power(a, f) * (-np.power(a, d) - np.power(a, g) * x[2]) * (np.power(a, f) * x[0] - np.power(a, g) * x[1]
          * x[2]) + np.power(a, f)*(-np.power(a, d) - np.power(a, g) * x[2]) * (-np.power(a, f) * x[0]
          + np.power(t, 1 / p)) + np.power(a, f + g) * x[2]* (-np.power(a, d) * x[1] - np.power(a, g) * x[1] * x[2]
                                                              + np.power(t, 1 / q))

    H22 = -2 * np.power(a, g) * x[2] * (-np.power(a, d) - np.power(a, g) * x[2]) * (-np.power(a, f) * x[0]
                                                                                    + np.power(t, 1 / p))

    H23 = np.power(a, 2 * g) * x[2] * x[1]* (-np.power(a, f) * x[0] + np.power(t, 1 / p)) - np.power(a, g) \
          * (-np.power(a, d) - np.power(a, g) * x[2]) * x[1] * (-np.power(a, f) * x[0] + np.power(t, 1 / p)) \
          - np.power(a, g)*(np.power(a, f) * x[0] - np.power(a, g) * x[1] * x[2]) * (-np.power(a, f) * x[0]
          + np.power(t, 1 / p)) - np.power(a, g) * (-np.power(a, f) * x[0] + np.power(t, 1 / p)) \
          * (- np.power(a, d) * x[1] - np.power(a, g) * x[1] * x[2] + np.power(t, 1 / q))

    H31 = np.power(a, f + g) * x[1]*(np.power(a, f) * x[0] - np.power(a, g) * x[1] * x[2]) - np.power(a, f + g) \
          * x[1] * (-np.power(a, f) * x[0] + np.power(t, 1 / p)) + np.power(a, f + g) * x[1] * (-np.power(a, d)
          * x[1] - np.power(a, g) * x[1] * x[2] + np.power(t, 1 / q))

    H32 = np.power(a, 2 * g) * x[2] * x[1]* (-np.power(a, f) * x[0] + np.power(t, 1 / p)) - np.power(a, g) \
          * (-np.power(a, d) - np.power(a, g)* x[2]) * x[1]*(-np.power(a, f) * x[0] + np.power(t, 1 / p))
    - np.power(a, g) * (np.power(a, f) * x[0] - np.power(a, g) * x[2] * x[1])*(-np.power(a, f) * x[0]
    + np.power(t, 1 / p))- np.power(a, g) * (-np.power(a, f) * x[0] + np.power(t, 1 / p))*(
        -np.power(a, d) * x[1] - np.power(a, g) * x[1] * x[2] + np.power(t, 1 / q))

    H33 = 2 * np.power(a, 2 * g)* np.power(x[1], 2)*(-np.power(a, f) * x[0] + np.power(t, 1 / p))

    return np.array([[H11, H12, H13],
                     [H21, H22, H23],
                     [H31, H32, H33]])


def is_minimum(H):
    return all(eig > 0 for eig in eigvals(H))


def is_maximum(H):
    return all(eig < 0 for eig in eigvals(H))


def find_extrema(func, grad, hess, initial_guess):
    result = minimize(func, initial_guess, jac=grad, hess=hess, constraints=constraints, bounds=bounds, method='trust-constr')
    H = hess(result.x)

    if is_minimum(H):
        return "minimum", result.x
    elif is_maximum(H):
        return "maximum", result.x
    else:
        return "saddle point", result.x


extrema_type, extrema_coords = find_extrema(function, gradient, hessian, initial_guess)

print(f"Local {extrema_type} at {extrema_coords}")

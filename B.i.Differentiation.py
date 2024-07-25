#b) Using PYTHON show how the following is achieved(PRACTICAL)
#i. Differentiation

import numpy as np

# Define the function
def f(x):
    return x**2 + 3*x + 2

# Define the numerical derivative function
def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# Compute the derivative at specific points
x_values = np.array([1, 2, 3, 4, 5])
derivative_values = numerical_derivative(f, x_values)

# Print the results
print(derivative_values)

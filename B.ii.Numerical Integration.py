#b) Using PYTHON show how the following is achieved(PRACTICAL)
#ii. Numerical integration

import numpy as np

# Define the function
def f(x):
    return x**2 + 3*x + 2

# Generate the points
x = np.linspace(0, 5, 100)

# Evaluate the function at each point
y = f(x)

# Perform the integration using the trapezoidal rule
integral = np.trapz(y, x)

# Print the result
print("The integral result is:", integral)

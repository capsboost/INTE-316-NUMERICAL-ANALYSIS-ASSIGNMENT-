# g) Write a program to show how the trapezoidal rule of integration works in PYTHON (PRACTICAL) 

import numpy as np

# Define the function to integrate
def f(x):
    return x ** 2 # Example function: f(x) = x^2

# Implementing the trapezoidal rule
def trapezoidal_rule(a, b, n):
    h = (b - a) / n # Step size
    integration = (f(a) + f(b)) / 2.0 # Initial sum with first and last terms

    for i in range(1, n):
        integration += f(a + i * h) # Sum the middle terms

    integration *= h # Multiply by step size
    return integration

# Define the limits of integration and number of subintervals
a = 0 # Lower limit
b = 1 # Upper limit
n = 100 # Number of subintervals

# Calculate the integral
result = trapezoidal_rule(a, b, n)
print(f"Approximate value of the integral: {result}")
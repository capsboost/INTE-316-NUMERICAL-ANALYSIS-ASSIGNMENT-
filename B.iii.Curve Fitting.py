#b) Using PYTHON show how the following is achieved(PRACTICAL)
#iii. Curve Fitting

import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x_data = np.linspace(0, 10, 100)
y_data = 3.5 * np.sin(x_data) + np.random.normal(size=x_data.size)

# Define the degree of the polynomial
degree = 3

# Fit the polynomial to the data
coefficients = np.polyfit(x_data, y_data, degree)

# Generate the fitted curve
y_fit = np.polyval(coefficients, x_data)

# Plot data and fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, y_fit, color='red', label='Fitted curve')
plt.legend()
plt.show()

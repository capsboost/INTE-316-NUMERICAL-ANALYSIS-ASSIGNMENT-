#b) Using PYTHON show how the following is achieved(PRACTICAL)
#v. Spline Interpolation
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Generate some data
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Create the spline interpolator
spline = make_interp_spline(x, y)

# Generate new x values for interpolation
x_new = np.linspace(0, 10, 300)
y_new = spline(x_new)

# Plot data and interpolated curve
plt.scatter(x, y, label='Data')
plt.plot(x_new, y_new, color='red', label='Spline interpolation')
plt.legend()
plt.show()

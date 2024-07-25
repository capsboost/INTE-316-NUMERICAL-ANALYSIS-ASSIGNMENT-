#b) Using PYTHON show how the following is achieved(PRACTICAL)
#iv. Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate some data
np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# Create and train the model
model = LinearRegression()
model.fit(x, y)

# Make predictions
x_new = np.array([[0], [2]])
y_predict = model.predict(x_new)

# Plot data and regression line
plt.scatter(x, y, label='Data')
plt.plot(x_new, y_predict, color='red', label='Regression line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#C) A smart robotic agent with a laser Scanner is doing a quick quality check on holes drilled 
#in a rectangular plate. The centers of the hole in the plate describes the path the arm 
#needs to take, and the hole centers are located on a Cartesian coordinate system as shown 
#X (in) 2.00 4.25 5.25 7.81 9.20 10.60
#Y(in) 7.2 7.1 6.0 5.0 3.5 5.0
#If the laser scanner is traversing from x=2.00 to x =4.25 in a linear path, what is the value 
#of y at x= 4.0 using the linear spline formula , show how this problem can be solved using 
#PYTHON (PRACTICAL) 

import numpy as np

# Given data points
x_points = np.array([2.00, 4.25])
y_points = np.array([7.2, 7.1])

# Point to interpolate
x_to_interpolate = 4.0

# Linear interpolation formula
y_interpolated = y_points[0] + (y_points[1] - y_points[0]) * (x_to_interpolate - x_points[0]) / (x_points[1] - x_points[0])
print(f"The value of y at x = {x_to_interpolate} is {y_interpolated :.2f}")
# matrix_interpolation_example.py
import numpy as np
from scipy.interpolate import interp2d

# Example data points
x = np.array([0, 1, 2])
y = np.array([0, 1, 2])
z = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Interpolate missing values
interpolator = interp2d(x, y, z, kind='linear')
interpolated_values = interpolator(x, y)

# Display the results
print("Original Matrix:")
print(z)
print("\nInterpolated Matrix:")
print(interpolated_values)

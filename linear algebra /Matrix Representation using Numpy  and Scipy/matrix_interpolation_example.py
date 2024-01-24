# matrix_interpolation_example.py
import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt

# Example matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Interpolation function
interp_func = interp2d(range(matrix.shape[1]), range(matrix.shape[0]), matrix, kind='linear')

# Interpolate values at new points
new_points = np.array([[1.5, 2.5],
                       [0.5, 1.5]])
interpolated_values = interp_func(new_points[:, 0], new_points[:, 1])

# Display the results
print("Example Matrix:")
print(matrix)
print("\nInterpolated Values:")
print(interpolated_values)

# Plotting the original and interpolated matrices
plt.imshow(matrix, cmap='viridis', interpolation='none', extent=(0, matrix.shape[1], matrix.shape[0], 0))
plt.scatter(new_points[:, 0], new_points[:, 1], color='red', marker='x')
plt.title('Matrix Interpolation')
plt.show()

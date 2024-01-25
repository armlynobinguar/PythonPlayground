# matrix_differentiation_example.py
import numpy as np
from scipy.misc import derivative

# Example matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Function for differentiation
def func(x):
    return np.interp(x, range(matrix.shape[1]), matrix[0, :])

# Compute derivative along the first row
derivative_values = np.array([derivative(func, x0, dx=1e-6) for x0 in range(matrix.shape[1])])

# Display the results
print("Example Matrix:")
print(matrix)
print("\nDerivative Values:")
print(derivative_values)


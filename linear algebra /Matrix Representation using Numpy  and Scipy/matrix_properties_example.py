import numpy as np
from matrix_representation.utils.matrix_operations import matrix_properties

# Example usage
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get matrix properties
properties = matrix_properties(matrix)
print("Matrix Properties:")
print(properties)

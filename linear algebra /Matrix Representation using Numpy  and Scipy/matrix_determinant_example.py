import numpy as np
from matrix_representation.utils.matrix_operations import matrix_determinant

# Example usage
matrix = np.array([[4, 7], [2, 6]])

# Find the determinant of the matrix
determinant = matrix_determinant(matrix)
print("Original Matrix:")
print(matrix)
print("Determinant:", determinant)

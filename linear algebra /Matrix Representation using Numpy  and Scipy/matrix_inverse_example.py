import numpy as np
from matrix_representation.utils.matrix_operations import inverse_matrix

# Example usage
matrix = np.array([[4, 7], [2, 6]])

# Find the inverse of the matrix
inverse = inverse_matrix(matrix)
print("Original Matrix:")
print(matrix)
print("Inverse Matrix:")
print(inverse)

import numpy as np
from matrix_representation.utils.matrix_operations import transpose_matrix

# Example usage
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Find the transpose of the matrix
transpose = transpose_matrix(matrix)
print("Original Matrix:")
print(matrix)
print("Transpose Matrix:")
print(transpose)

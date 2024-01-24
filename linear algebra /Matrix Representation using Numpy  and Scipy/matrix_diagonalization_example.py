import numpy as np
from matrix_representation.utils.matrix_operations import diagonalize_matrix

# Example usage
matrix = np.array([[4, 2], [1, 3]])

# Diagonalize the matrix
diagonalized_matrix, diagonal_matrix = diagonalize_matrix(matrix)
print("Original Matrix:")
print(matrix)
print("Diagonalized Matrix:")
print(diagonalized_matrix)
print("Diagonal Matrix:")
print(diagonal_matrix)

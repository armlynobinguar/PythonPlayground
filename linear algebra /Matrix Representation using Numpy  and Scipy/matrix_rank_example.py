import numpy as np
from matrix_representation.utils.matrix_operations import matrix_rank

# Example usage
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Find the rank of the matrix
rank = matrix_rank(matrix)
print("Original Matrix:")
print(matrix)
print("Rank:", rank)

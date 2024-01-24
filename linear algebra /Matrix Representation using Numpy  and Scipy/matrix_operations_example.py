import numpy as np
from matrix_representation.utils.matrix_operations import add_matrices, multiply_matrices

# Example matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix addition
result_addition = add_matrices(matrix1, matrix2)
print("Matrix Addition Result:")
print(result_addition)

# Matrix multiplication
result_multiplication = multiply_matrices(matrix1, matrix2)
print("\nMatrix Multiplication Result:")
print(result_multiplication)

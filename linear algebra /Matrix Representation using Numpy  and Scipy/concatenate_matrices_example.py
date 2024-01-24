import numpy as np

# Example matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Concatenate matrices horizontally and vertically
horizontal_concatenation = np.concatenate((matrix1, matrix2), axis=1)
vertical_concatenation = np.concatenate((matrix1, matrix2), axis=0)

# Display results
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nHorizontal Concatenation Result:")
print(horizontal_concatenation)
print("\nVertical Concatenation Result:")
print(vertical_concatenation)

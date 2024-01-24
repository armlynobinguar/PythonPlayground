import numpy as np

# Example matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extract submatrix
submatrix = matrix[1:, :2]

# Display results
print("Original Matrix:")
print(matrix)
print("\nExtracted Submatrix:")
print(submatrix)

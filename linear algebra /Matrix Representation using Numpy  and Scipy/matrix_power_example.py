import numpy as np

# Example matrix
matrix = np.array([[1, 2], [3, 4]])

# Matrix power
power = 2
result = np.linalg.matrix_power(matrix, power)

# Display results
print("Original Matrix:")
print(matrix)
print("\nMatrix Power Result (matrix^2):")
print(result)

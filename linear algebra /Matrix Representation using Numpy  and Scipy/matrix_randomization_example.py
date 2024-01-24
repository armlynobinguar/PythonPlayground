# matrix_randomization_example.py
import numpy as np

# Example matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Randomize the matrix
randomized_matrix = np.random.permutation(matrix)

# Display the results
print("Example Matrix:")
print(matrix)
print("\nRandomized Matrix:")
print(randomized_matrix)

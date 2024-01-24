# matrix_norms_example.py
import numpy as np

# Example matrix
matrix = np.array([[1, 2], [3, 4]])

# Frobenius norm
frobenius_norm = np.linalg.norm(matrix, 'fro')

# Other norms
l1_norm = np.linalg.norm(matrix, 1)
l2_norm = np.linalg.norm(matrix, 2)
infinity_norm = np.linalg.norm(matrix, np.inf)

# Display the results
print("Example Matrix:")
print(matrix)
print(f"\nFrobenius Norm: {frobenius_norm}")
print(f"L1 Norm: {l1_norm}")
print(f"L2 Norm: {l2_norm}")
print(f"Infinity Norm: {infinity_norm}")

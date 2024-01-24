# matrix_compression_example.py
import numpy as np
from scipy.linalg import svd

# Example matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Perform SVD for compression
u, s, vh = svd(matrix, full_matrices=False)

# Rank-k approximation
k = 2
compressed_matrix = u[:, :k] @ np.diag(s[:k]) @ vh[:k, :]

# Display the results
print("Example Matrix:")
print(matrix)
print(f"\nCompressed Matrix (Rank-{k} Approximation):")
print(compressed_matrix)

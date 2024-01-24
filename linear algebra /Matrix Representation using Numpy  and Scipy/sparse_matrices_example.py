# sparse_matrices_example.py
import numpy as np
from scipy.sparse import csr_matrix

# Example dense matrix
dense_matrix = np.array([[0, 0, 1], [0, 2, 0], [3, 0, 4]])

# Convert to sparse matrix
sparse_matrix = csr_matrix(dense_matrix)

# Display the results
print("Example Dense Matrix:")
print(dense_matrix)
print("\nConverted Sparse Matrix:")
print(sparse_matrix.toarray())

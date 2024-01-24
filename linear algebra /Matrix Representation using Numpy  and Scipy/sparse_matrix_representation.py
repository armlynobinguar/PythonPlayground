import numpy as np
from scipy.sparse import csr_matrix

# Example sparse matrix representation
sparse_matrix = csr_matrix([[0, 0, 1, 0], [0, 2, 0, 0], [0, 0, 0, 3]])

print("Sparse Matrix:")
print(sparse_matrix.toarray())

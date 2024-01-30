import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

def sparse_gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian elimination for sparse matrices.

    Args:
    A (scipy.sparse.csr_matrix): Sparse coefficient matrix in CSR format.
    b (numpy.ndarray): Right-hand side vector.

    Returns:
    x (numpy.ndarray): Solution vector.
    """
    # Convert A to CSR format if it's not already
    if not isinstance(A, csr_matrix):
        A = csr_matrix(A)

    # Solve using SciPy's sparse matrix solver
    x = spsolve(A, b)

    return x

# Example usage
A = np.array([
    [3, 0, 0],
    [2, 3, 0],
    [0, 1, 4]
])
b = np.array([9, 8, 3])

# Convert A to CSR format
A_sparse = csr_matrix(A)

# Solve the sparse system
x = sparse_gaussian_elimination(A_sparse, b)
print("Solution:", x)

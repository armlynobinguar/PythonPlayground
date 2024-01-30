import numpy as np

def optimized_gaussian_elimination(A, b):
    """
    Solves the system Ax = b using a performance-optimized Gaussian elimination.

    Args:
    A (numpy.ndarray): Coefficient matrix.
    b (numpy.ndarray): Right-hand side vector.

    Returns:
    x (numpy.ndarray): Solution vector.
    """
    n = len(A)
    A = A.astype(float)  # Ensure floating-point precision
    b = b.astype(float)

    # Forward Elimination
    for i in range(n):
        # Pivoting for numerical stability
        max_row = np.argmax(np.abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Eliminate variable i from subsequent rows
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Back Substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

# Example usage
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)
b = np.array([8, -11, -3], dtype=float)

x = optimized_gaussian_elimination(A, b)
print("Solution:", x)

import numpy as np

def full_pivoting_elimination(A, b):
    """
    Solves Ax = b using Gaussian Elimination with Full Pivoting.

    Parameters:
    A (numpy.ndarray): Coefficient matrix
    b (numpy.ndarray): Right-hand side vector

    Returns:
    x (numpy.ndarray): Solution vector
    """
    n = len(A)
    A = A.astype(float)
    b = b.astype(float)
    col_index = np.arange(n)

    # Forward elimination with full pivoting
    for k in range(n-1):
        # Find the pivot element
        pivot_row, pivot_col = np.unravel_index(np.argmax(np.abs(A[k:, k:])), A[k:, k:].shape)
        pivot_row += k
        pivot_col += k

        # Swap rows
        A[[k, pivot_row]] = A[[pivot_row, k]]
        b[[k, pivot_row]] = b[[pivot_row, k]]

        # Swap columns
        A[:, [k, pivot_col]] = A[:, [pivot_col, k]]
        col_index[k], col_index[pivot_col] = col_index[pivot_col], col_index[k]

        # Elimination process
        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    # Backward substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    # Reorder solution to original column order
    x_final = np.zeros(n)
    for i in range(n):
        x_final[col_index[i]] = x[i]

    return x_final

# Example usage
if __name__ == "__main__":
    A = np.array([[0, 2, 3], [4, 5, 6], [7, 0, 9]], dtype=float)
    b = np.array([1, 2, 3], dtype=float)
    x = full_pivoting_elimination(A, b)
    print("Solution:", x)

import numpy as np

def gaussian_elimination(A, b):
    """
    Perform Gaussian elimination to solve Ax = b.

    Args:
        A (numpy.ndarray): Coefficient matrix.
        b (numpy.ndarray): Right-hand side vector.

    Returns:
        numpy.ndarray: Solution vector x.
    """
    n = len(b)
    M = np.hstack([A, b.reshape(-1, 1)])  # Augmented matrix

    # Forward elimination
    for i in range(n):
        # Pivot for column
        max_row = np.argmax(np.abs(M[i:n, i])) + i
        M[[i, max_row]] = M[[max_row, i]]  # Swap rows

        # Eliminate below
        for j in range(i + 1, n):
            factor = M[j, i] / M[i, i]
            M[j, i:] -= factor * M[i, i:]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i + 1:n], x[i + 1:n])) / M[i, i]

    return x

# Example usage
if __name__ == "__main__":
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)
    b = np.array([8, -11, -3], dtype=float)
    
    solution = gaussian_elimination(A, b)
    print("Solution:", solution)

import numpy as np

def scaled_partial_pivoting_gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian elimination with scaled partial pivoting.

    Args:
    A (numpy.ndarray): Coefficient matrix.
    b (numpy.ndarray): Right-hand side vector.

    Returns:
    x (numpy.ndarray): Solution vector.
    """
    n = len(b)
    x = np.zeros(n)
    s = np.zeros(n)
    p = np.arange(n)

    # Scale factors
    for i in range(n):
        s[i] = max(abs(A[i, :]))

    for k in range(n - 1):
        # Partial pivoting
        p_max = abs(A[p[k], k]/s[p[k]])
        k_max = k
        for i in range(k + 1, n):
            if abs(A[p[i], k]/s[p[i]]) > p_max:
                p_max = abs(A[p[i], k]/s[p[i]])
                k_max = i

        # Swap rows
        p[k], p[k_max] = p[k_max], p[k]

        # Elimination
        for i in range(k + 1, n):
            factor = A[p[i], k] / A[p[k], k]
            A[p[i], k+1:] -= factor * A[p[k], k+1:]
            b[p[i]] -= factor * b[p[k]]

    # Back substitution
    for i in range(n - 1, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += A[p[i], j] * x[j]
        x[i] = (b[p[i]] - sum_ax) / A[p[i], i]

    return x

# Example usage
A = np.array([[3., -0.1, -0.2], [0.1, 7., -0.3], [0.3, -0.2, 10.]])
b = np.array([7.85, -19.3, 71.4])
x = scaled_partial_pivoting_gaussian_elimination(A, b)
print("Solution:", x)

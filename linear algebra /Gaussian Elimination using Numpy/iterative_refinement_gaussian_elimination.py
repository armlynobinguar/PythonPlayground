import numpy as np

def gaussian_elimination(A, b):
    """
    Performs Gaussian elimination without pivoting.

    Args:
    A (numpy.ndarray): Coefficient matrix.
    b (numpy.ndarray): Right-hand side vector.

    Returns:
    x (numpy.ndarray): Solution vector.
    """
    n = len(A)
    # Forward elimination
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i][i]

    return x

def iterative_refinement(A, b, x, iterations=10):
    # Iterative refinement code (unchanged)
    # ...

# Example usage
A = np.array([
    [3, 2, -4],
    [2, 3, 3],
    [5, -3, 1]
], dtype=float)
b = np.array([3, 15, 14], dtype=float)

# Initial solution using Gaussian elimination
initial_x = gaussian_elimination(A, b)

# Refine the solution
refined_x = iterative_refinement(A, b, initial_x)
print("Refined Solution:", refined_x)

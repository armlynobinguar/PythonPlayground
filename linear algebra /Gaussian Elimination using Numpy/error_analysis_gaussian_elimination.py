import numpy as np

def gaussian_elimination(A, b):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += A[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i][i]

    return x

def compute_residual(A, x, b):
    """Computes the residual vector r = b - Ax."""
    r = b - np.dot(A, x)
    return r

def compute_relative_error(x, x_true):
    """Computes the relative error between the computed solution x and the true solution x_true."""
    error = np.linalg.norm(x - x_true, np.inf) / np.linalg.norm(x_true, np.inf)
    return error

# Example usage
A = np.array([[3, 2, -4], [2, 3, 3], [5, -3, 1]], dtype=float)
b = np.array([3, 15, 14], dtype=float)
x_true = np.linalg.solve(A, b)  # True solution for comparison

x = gaussian_elimination(A.copy(), b.copy())
residual = compute_residual(A, x, b)
relative_error = compute_relative_error(x, x_true)

print("Computed Solution:", x)
print("Residual:", residual)
print("Relative Error:", relative_error)

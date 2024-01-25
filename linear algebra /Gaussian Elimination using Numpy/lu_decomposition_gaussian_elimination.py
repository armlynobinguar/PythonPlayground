import numpy as np

def lu_decomposition(A):
    """
    Performs LU Decomposition on matrix A.

    Parameters:
    A (numpy.ndarray): The matrix to decompose

    Returns:
    L (numpy.ndarray): Lower triangular matrix
    U (numpy.ndarray): Upper triangular matrix
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # LU Decomposition
    for i in range(n):
        # Upper Triangular
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_

        # Lower Triangular
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Diagonal as 1
            else:
                sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_) / U[i][i]

    return L, U

# Example usage
if __name__ == "__main__":
    A = np.array([[2, -1, -2], [-4, 6, 3], [-4, -2, 8]], dtype=float)
    L, U = lu_decomposition(A)
    print("L:", L)
    print("U:", U)

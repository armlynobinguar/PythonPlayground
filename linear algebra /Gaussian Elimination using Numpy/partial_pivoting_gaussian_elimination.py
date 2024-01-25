import numpy as np

def partial_pivoting_elimination(A, b):
    """
    Solves Ax = b using Gaussian Elimination with Partial Pivoting.
    
    Parameters:
    A (numpy.ndarray): Coefficient matrix
    b (numpy.ndarray): Right-hand side vector

    Returns:
    x (numpy.ndarray): Solution vector
    """
    n = len(A)
    A = A.astype(float)
    b = b.astype(float)

    # Forward elimination with partial pivoting
    for k in range(n-1):
        # Find the pivot row
        max_index = np.argmax(np.abs(A[k:, k])) + k
        # Swap the rows
        A[[k, max_index]] = A[[max_index, k]]
        b[[k, max_index]] = b[[max_index, k]]

        # Elimination process
        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

    # Backward substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x

# Example usage
if __name__ == "__main__":
    A = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]])
    b = np.array([4, 5, 6])
    x = partial_pivoting_elimination(A, b)
    print("Solution:", x)

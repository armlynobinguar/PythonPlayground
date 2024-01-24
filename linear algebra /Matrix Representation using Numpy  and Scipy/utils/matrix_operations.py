import numpy as np

def add_matrices(matrix1, matrix2):
    """
    Add two matrices.

    Args:
        matrix1 (numpy.ndarray): First matrix.
        matrix2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray or None: Resultant matrix after addition if matrices are compatible, None otherwise.
    """
    if matrix1.shape != matrix2.shape:
        print("Error: Matrices must have the same shape for addition.")
        return None
    return np.add(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices.

    Args:
        matrix1 (numpy.ndarray): First matrix.
        matrix2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray or None: Resultant matrix after multiplication if matrices are compatible, None otherwise.
    """
    if matrix1.shape[1] != matrix2.shape[0]:
        print("Error: Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
        return None
    return np.dot(matrix1, matrix2)

import numpy as np

def add_matrices(matrix1, matrix2):
    """
    Add two matrices.

    Args:
        matrix1 (numpy.ndarray): First matrix.
        matrix2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: Resultant matrix after addition.
    """
    return np.add(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices.

    Args:
        matrix1 (numpy.ndarray): First matrix.
        matrix2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: Resultant matrix after multiplication.
    """
    return np.dot(matrix1, matrix2)

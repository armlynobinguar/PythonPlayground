# matrix_operations.py
import numpy as np

def create_identity_matrix(size):
    """
    Create an identity matrix of given size.

    Args:
        size (int): Size of the identity matrix.

    Returns:
        numpy.ndarray: Identity matrix.
    """
    return np.eye(size)

def scalar_multiply_matrix(matrix, scalar):
    """
    Multiply a matrix by a scalar.

    Args:
        matrix (numpy.ndarray): Input matrix.
        scalar (float): Scalar value.

    Returns:
        numpy.ndarray: Resultant matrix after scalar multiplication.
    """
    return scalar * matrix

def elementwise_multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices element-wise.

    Args:
        matrix1 (numpy.ndarray): First matrix.
        matrix2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: Resultant matrix after element-wise multiplication.
    """
    return np.multiply(matrix1, matrix2)

def matrix_power(matrix, power):
    """
    Raise a matrix to a specified power.

    Args:
        matrix (numpy.ndarray): Input matrix.
        power (int): Power to which the matrix is raised.

    Returns:
        numpy.ndarray: Resultant matrix after raising to the power.
    """
    return np.linalg.matrix_power(matrix, power)

def concatenate_matrices(matrix1, matrix2, axis=0):
    """
    Concatenate two matrices along a specified axis.

    Args:
        matrix1 (numpy.ndarray): First matrix.
        matrix2 (numpy.ndarray): Second matrix.
        axis (int, optional): Axis along which matrices are concatenated (default is 0).

    Returns:
        numpy.ndarray: Concatenated matrix.
    """
    return np.concatenate((matrix1, matrix2), axis=axis)

def extract_submatrix(matrix, row_indices, col_indices):
    """
    Extract a submatrix from the given matrix.

    Args:
        matrix (numpy.ndarray): Input matrix.
        row_indices (list): List of row indices to extract.
        col_indices (list): List of column indices to extract.

    Returns:
        numpy.ndarray: Submatrix extracted from the original matrix.
    """
    return matrix[row_indices][:, col_indices]

# Add other matrix operations functions here...

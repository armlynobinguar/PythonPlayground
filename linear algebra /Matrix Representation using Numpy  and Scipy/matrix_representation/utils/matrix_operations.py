import numpy as np

def create_matrix(rows, cols, values):
    """
    Create a matrix with specified values.

    Args:
        rows (int): Number of rows in the matrix.
        cols (int): Number of columns in the matrix.
        values (list): List of lists containing the matrix elements.

    Returns:
        numpy.ndarray: Created matrix.
    """
    return np.array(values)

def matrix_properties(matrix):
    """
    Get properties of a matrix.

    Args:
        matrix (numpy.ndarray): Input matrix.

    Returns:
        dict: Dictionary containing matrix properties.
    """
    properties = {
        "Shape": matrix.shape,
        "Rank": np.linalg.matrix_rank(matrix),
        "Determinant": np.linalg.det(matrix),
        "Inverse Exists": np.linalg.matrix_rank(matrix) == matrix.shape[0] == matrix.shape[1],
        "Transpose": matrix.T
    }
    return properties

def inverse_matrix(matrix):
    """
    Compute the inverse of a matrix.

    Args:
        matrix (numpy.ndarray): Input matrix.

    Returns:
        numpy.ndarray: Inverse matrix.
    """
    if np.linalg.matrix_rank(matrix) == matrix.shape[0] == matrix.shape[1]:
        return np.linalg.inv(matrix)
    else:
        raise ValueError("Matrix is singular or not square; cannot compute the inverse.")

def transpose_matrix(matrix):
    """
    Compute the transpose of a matrix.

    Args:
        matrix (numpy.ndarray): Input matrix.

    Returns:
        numpy.ndarray: Transposed matrix.
    """
    return matrix.T

def matrix_determinant(matrix):
    """
    Compute the determinant of a matrix.

    Args:
        matrix (numpy.ndarray): Input matrix.

    Returns:
        float: Determinant of the matrix.
    """
    return np.linalg.det(matrix)

def matrix_rank(matrix):
    """
    Compute the rank of a matrix.

    Args:
        matrix (numpy.ndarray): Input matrix.

    Returns:
        int: Rank of the matrix.
    """
    return np.linalg.matrix_rank(matrix)

def solve_linear_system(coefficients, constants):
    """
    Solve a system of linear equations.

    Args:
        coefficients (numpy.ndarray): Coefficients matrix.
        constants (numpy.ndarray): Constants vector.

    Returns:
        numpy.ndarray: Solution vector.
    """
    return np.linalg.solve(coefficients, constants)

def diagonalize_matrix(matrix):
    """
    Diagonalize a matrix.

    Args:
        matrix (numpy.ndarray): Input matrix.

    Returns:
        numpy.ndarray: Diagonalized matrix.
        numpy.ndarray: Diagonal matrix.
    """
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    diagonal_matrix = np.diag(eigenvalues)
    diagonalized_matrix = np.dot(np.dot(np.linalg.inv(eigenvectors), matrix), eigenvectors)
    return diagonalized_matrix, diagonal_matrix

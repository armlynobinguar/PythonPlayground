import numpy as np

class LinearAlgebraSolver:
    @staticmethod
    def solve_system(coefficients, constants):
        # Solve a system of linear equations
        solution = np.linalg.solve(coefficients, constants)
        return solution

    @staticmethod
    def compute_determinant(matrix):
        # Compute the determinant of a matrix
        determinant = np.linalg.det(matrix)
        return determinant

    @staticmethod
    def compute_inverse(matrix):
        # Compute the inverse of a matrix
        inverse_matrix = np.linalg.inv(matrix)
        return inverse_matrix

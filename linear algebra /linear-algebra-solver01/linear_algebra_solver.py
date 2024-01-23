import numpy as np

class LinearAlgebraSolver:
    def solve_linear_system(self, coefficients, constants):
        """
        Solve a system of linear equations using numpy's linear algebra solver.

        Args:
            coefficients (ndarray): Coefficients matrix (2D array).
            constants (ndarray): Constants vector (1D array).

        Returns:
            solution (ndarray): Solution vector.
        """
        try:
            # Step 1: Convert input to numpy arrays
            A = np.array(coefficients)
            B = np.array(constants)

            # Step 2: Use numpy's linear algebra solver to find the solution
            solution = np.linalg.solve(A, B)

            return solution

        except np.linalg.LinAlgError:
            # Handle the case where the system is singular or not solvable
            print("The system of equations is singular or not solvable.")
            return None

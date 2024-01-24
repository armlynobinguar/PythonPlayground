# systems_of_linear_equations.py
"""
Solving systems of linear equations with multiple variables.
Using NumPy for solving systems of equations.
"""

import numpy as np

def solve_linear_system(coefficients, constants):
    """
    Solve a system of linear equations using NumPy.

    Args:
        coefficients (ndarray): Coefficients matrix (2D array).
        constants (ndarray): Constants vector (1D array).

    Returns:
        ndarray or None: Solution vector if a solution exists, None otherwise.
    """
    try:
        # Convert input to numpy arrays
        A = np.array(coefficients)
        B = np.array(constants)

        # Use NumPy's linear algebra solver to find the solution
        solution = np.linalg.solve(A, B)

        return solution

    except np.linalg.LinAlgError:
        # Handle the case where the system is singular or not solvable
        print("The system of equations is singular or not solvable.")
        return None

def solve_system_example():
    """
    Example usage of solving a system of linear equations.
    """
    # Example system of linear equations:
    # 2x + y = 8
    # 3x - 2y = -11
    coefficients = np.array([[2, 1], [3, -2]])
    constants = np.array([8, -11])

    # Solve the system
    solution = solve_linear_system(coefficients, constants)

    if solution is not None:
        print("Solution:")
        print("x =", solution[0])
        print("y =", solution[1])

if __name__ == "__main__":
    solve_system_example()

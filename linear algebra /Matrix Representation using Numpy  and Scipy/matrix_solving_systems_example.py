import numpy as np
from matrix_representation.utils.matrix_operations import solve_linear_system

# Example usage
coefficients = np.array([[2, 3], [1, -1]])
constants = np.array([8, 2])

# Solve the system of linear equations
solution = solve_linear_system(coefficients, constants)
print("Coefficients Matrix:")
print(coefficients)
print("Constants Vector:")
print(constants)
print("Solution Vector:")
print(solution)

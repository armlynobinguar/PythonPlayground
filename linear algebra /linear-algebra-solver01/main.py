from linear_algebra_solver import LinearAlgebraSolver

def main():
    # Example usage
    coefficients = np.array([[2, 1], [1, -1]])
    constants = np.array([8, -1])

    # Solve a system of linear equations
    solution = LinearAlgebraSolver.solve_system(coefficients, constants)
    print(f'Solution: {solution}')

    # Compute determinant
    determinant = LinearAlgebraSolver.compute_determinant(coefficients)
    print(f'Determinant: {determinant}')

    # Compute inverse
    inverse_matrix = LinearAlgebraSolver.compute_inverse(coefficients)
    print(f'Inverse Matrix:\n{inverse_matrix}')

if __name__ == "__main__":
    main()

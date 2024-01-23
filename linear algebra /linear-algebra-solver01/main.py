from linear_algebra_solver.linear_algebra_solver import LinearAlgebraSolver

if __name__ == "__main__":
    # Example usage
    solver = LinearAlgebraSolver()

    # Example system of linear equations:
    # 2x + y = 8
    # 3x - 2y = -11
    coefficients = [[2, 1], [3, -2]]
    constants = [8, -11]

    # Solve the system
    solution = solver.solve_linear_system(coefficients, constants)

    if solution is not None:
        print("Solution:")
        print("x =", solution[0])
        print("y =", solution[1])

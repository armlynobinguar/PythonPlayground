import numpy as np

# Linear Equation Lesson and Code

def lesson():
    print("Linear Equations Lesson:")
    print("A linear equation is an equation of the form Ax + By = C, where A, B, and C are constants.")
    print("The solution to a linear equation is the set of values (x, y) that satisfies the equation.")

def solve_linear_equation(A, B, C):
    try:
        # Check for division by zero
        if A == 0 and B == 0:
            raise ZeroDivisionError("Error: Both coefficients A and B cannot be zero.")

        # Solve for x and y
        x = (C - B) / A if A != 0 else None
        y = (C - A) / B if B != 0 else None
        return x, y

    except ZeroDivisionError as e:
        print(str(e))
        return None

def solve_simple_linear_equation():
    A = 3
    B = 0
    C = -4 + 5
    solution = solve_linear_equation(A, B, C)
    if solution:
        x = solution[0]
        print(f"Example 1: x = {x}")

def solve_one_variable_equation():
    # Example 2: Solving a linear equation with one variable: 2x - 7 = 3
    A = 2
    B = 0
    C = -7 + 3
    solution = solve_linear_equation(A, B, C)
    if solution:
        x = solution[0]
        print(f"Example 2: x = {x}")

def solve_two_variable_equation():
    # Example 3: Solving a linear equation with two variables: 3x - 2y = 7
    A = 3
    B = -2
    C = 7
    solution = solve_linear_equation(A, B, C)
    if solution:
        x, y = solution
        print(f"Example 3: x = {x}, y = {y}")

def solve_equation_with_constants():
    # Example 4: Solving a linear equation with constants on both sides: 4x + 2 = 2x + 6
    A = 2
    B = -2
    C = 6 - 2
    solution = solve_linear_equation(A, B, C)
    if solution:
        x = solution[0]
        print(f"Example 4: x = {x}")

if __name__ == "__main__":
    # Example usage
    lesson()

    # Example linear equation: 2x + 3y = 12
    A = 2
    B = 3
    C = 12

    # Solve the linear equation
    solution = solve_linear_equation(A, B, C)

    if solution:
        print("\nSolution:")
        print("x =", solution[0])
        print("y =", solution[1])

    # Other examples
    solve_simple_linear_equation()
    solve_one_variable_equation()
    solve_two_variable_equation()
    solve_equation_with_constants()

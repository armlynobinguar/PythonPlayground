import numpy as np

# Linear Equation Lesson and Code

def lesson():
    print("Linear Equations Lesson:")
    print("A linear equation is an equation of the form Ax + By = C, where A, B, and C are constants.")
    print("The solution to a linear equation is the set of values (x, y) that satisfies the equation.")

def solve_linear_equation(A, B, C):
    try:
        # Solve for x and y
        x = (C - B) / A
        y = (C - A) / B
        return x, y
    except ZeroDivisionError:
        print("Error: Division by zero. The coefficients A and B cannot be zero.")

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

    # Example 1: Solving a simple linear equation: 3x - 4 = 5
    def solve_simple_linear_equation():
        A = 3
        B = 0
        C = -4 + 5
        x = solve_linear_equation(A, B, C)[0]
        print(f"Example 1: x = {x}")

    # Other examples...

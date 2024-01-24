import numpy as np

# Linear Equation Lesson and Code (Google Colab)

def lesson():
    print("Linear Equations Lesson:")
    print("A linear equation is an equation of the form Ax + By = C, where A, B, and C are constants.")
    print("The solution to a linear equation is the set of values (x, y) that satisfies the equation.")
    print("\nCreating a Linear Equation:")
    print("You can create a linear equation in the form Ax + By = C.")
    print("For example, the equation 2x - 3y = 5 can be represented as:")
    print("A = 2, B = -3, C = 5\n")

def create_linear_equation(A, B, C):
    return f"{A}x + {B}y = {C}"

def solve_linear_equation(A, B, C):
    try:
        # Solve for x and y
        x = (C - B) / A
        y = (C - A) / B
        return x, y
    except ZeroDivisionError:
        print("Error: Division by zero. The coefficients A and B cannot be zero.")

def print_example_equations():
    print("\nAdditional Examples of Linear Equations:")
    examples = [
        (3, 4, 15),  # 3x + 4y = 15
        (-2, 5, 8),  # -2x + 5y = 8
        (1, -1, 0),  # x - y = 0
    ]
    for example in examples:
        equation = create_linear_equation(*example)
        print(f"{equation}")

if __name__ == "__main__":
    # Example usage
    lesson()

    # Example linear equation: 2x + 3y = 12
    A = 2
    B = 3
    C = 12

    # Create a linear equation
    created_equation = create_linear_equation(A, B, C)
    print(f"Created Linear Equation: {created_equation}")

    # Solve the linear equation
    solution = solve_linear_equation(A, B, C)

    if solution:
        print("\nSolution:")
        print("x =", solution[0])
        print("y =", solution[1])

    # Print additional examples
    print_example_equations()

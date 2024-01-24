# simple_linear_equations.py
"""
Solving basic linear equations of the form Ax + By = C.
"""

def solve_linear_equation(A, B, C):
    """
    Solve a simple linear equation of the form Ax + By = C.

    Args:
        A (float): Coefficient of x.
        B (float): Coefficient of y.
        C (float): Constant term.

    Returns:
        tuple or None: (x, y) if a solution exists, None otherwise.
    """
    try:
        x = (C - B) / A
        y = (C - A) / B
        return x, y
    except ZeroDivisionError:
        print("Error: Division by zero. The coefficients A and B cannot be zero.")
        return None

def solve_simple_linear_equation():
    """
    Example usage of solving a simple linear equation.
    """
    # Example: 2x + 3y = 12
    A = 2
    B = 3
    C = 12

    # Solve the linear equation
    solution = solve_linear_equation(A, B, C)

    if solution:
        x, y = solution
        print("Solution:")
        print("x =", x)
        print("y =", y)

if __name__ == "__main__":
    solve_simple_linear_equation()

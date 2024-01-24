# equations_with_constants.py
"""
Handling equations with constants on both sides.
"""

def solve_equation_with_constants(A, B, C1, C2):
    """
    Solve an equation with constants on both sides: Ax + By = C1x + C2.

    Args:
        A (float): Coefficient of x on the left side.
        B (float): Coefficient of y on the left side.
        C1 (float): Constant term on the right side for x.
        C2 (float): Constant term on the right side.

    Returns:
        tuple or None: (x, y) if a solution exists, None otherwise.
    """
    try:
        x = (C2 - B) / (A - C1)
        y = (C2 - A * x) / B
        return x, y
    except ZeroDivisionError:
        print("Error: Division by zero. The coefficients A, B, and (A - C1) cannot be zero.")
        return None

def solve_equation_with_constants_example():
    """
    Example usage of solving an equation with constants on both sides.
    """
    # Example: 2x + 3y = 4x + 5
    A = 2
    B = 3
    C1 = 4
    C2 = 5

    # Solve the equation
    solution = solve_equation_with_constants(A, B, C1, C2)

    if solution:
        x, y = solution
        print("Solution:")
        print("x =", x)
        print("y =", y)

if __name__ == "__main__":
    solve_equation_with_constants_example()

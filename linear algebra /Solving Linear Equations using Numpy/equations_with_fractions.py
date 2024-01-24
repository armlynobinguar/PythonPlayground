# equations_with_fractions.py
"""
Solving equations with fractional coefficients.
"""

from fractions import Fraction

def solve_equation_with_fractions(A, B, C):
    """
    Solve an equation with fractional coefficients: Ax/2 + By/3 = C/4.

    Args:
        A (Fraction): Coefficient of x.
        B (Fraction): Coefficient of y.
        C (Fraction): Constant term.

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

def solve_equation_with_fractions_example():
    """
    Example usage of solving an equation with fractional coefficients.
    """
    # Example: x/2 + y/3 = 4/5
    A = Fraction(1, 2)
    B = Fraction(1, 3)
    C = Fraction(4, 5)

    # Solve the equation
    solution = solve_equation_with_fractions(A, B, C)

    if solution:
        x, y = solution
        print("Solution:")
        print("x =", x)
        print("y =", y)

if __name__ == "__main__":
    solve_equation_with_fractions_example()

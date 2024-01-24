# matrix_optimization_example.py
import numpy as np
from scipy.optimize import linprog

# Objective coefficients
c = np.array([-1, 2])

# Inequality constraints matrix
A = np.array([[1, 1], [-1, 2]])

# Inequality constraints vector
b = np.array([3, 2])

# Bounds
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds])

# Display the results
print("Optimal Values:")
print(result.x)
print("\nOptimal Objective Value:")
print(-result.fun)

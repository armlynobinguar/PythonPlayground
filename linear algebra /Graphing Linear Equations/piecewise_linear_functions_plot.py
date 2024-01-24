# piecewise_linear_functions_plot.py
import matplotlib.pyplot as plt
from utils.linear_equation_plotter import plot_piecewise_linear_functions

# Example usage
x_ranges = [(-10, -5), (-5, 0), (0, 5)]
slopes = [2, -1, 3]
intercepts = [5, 2, -1]

# Plot piecewise linear functions
plot_piecewise_linear_functions(x_ranges, slopes, intercepts)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Piecewise Linear Functions')
plt.grid(True)
plt.show()

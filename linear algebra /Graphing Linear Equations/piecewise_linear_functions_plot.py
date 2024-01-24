# piecewise_linear_functions_plot.py
import matplotlib.pyplot as plt
from utils.linear_equation_plotter import plot_piecewise_linear_functions

# Example usage
segments = [([-10, -5], 2, 5), ([-5, 0], -1, 2), ([0, 5], 3, -1)]

# Plot piecewise linear functions
plot_piecewise_linear_functions(segments)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Piecewise Linear Functions')
plt.grid(True)
plt.show()

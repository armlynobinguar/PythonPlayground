# point_slope_form_plot.py
import matplotlib.pyplot as plt
from utils.linear_equation_plotter import plot_point_slope_form

if __name__ == "__main__":
    # Example equation in point-slope form: y - y1 = m(x - x1)
    m = 2
    x1, y1 = 1, 3

    # Plot the equation in point-slope form
    plot_point_slope_form(m, x1, y1)

    # Add labels and title
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Point-Slope Form: y - {y1} = {m}(x - {x1})')

    # Display the plot
    plt.grid(True)
    plt.show()

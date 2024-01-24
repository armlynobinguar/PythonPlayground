from utils.linear_equation_plotter import plot_piecewise_linear_functions

if __name__ == "__main__":
    # Example piecewise linear functions
    segments = [((0, 2), 'y = x'), ((2, 4), 'y = -x + 4')]

    # Plot piecewise linear functions
    plot_piecewise_linear_functions(segments)

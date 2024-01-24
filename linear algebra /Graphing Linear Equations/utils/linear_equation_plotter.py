# linear_equation_plotter.py
import numpy as np
import matplotlib.pyplot as plt

def plot_simple_linear_equation(A, B, C):
    x = np.linspace(-10, 10, 100)
    y = (C - A * x) / B
    plt.plot(x, y, label=f'{A}x + {B}y = {C}')

def plot_slope_intercept_form(m, b):
    x = np.linspace(-10, 10, 100)
    y = m * x + b
    plt.plot(x, y, label=f'y = {m}x + {b}')

def plot_point_slope_form(m, x1, y1):
    x = np.linspace(-10, 10, 100)
    y = m * (x - x1) + y1
    plt.plot(x, y, label=f'y - {y1} = {m}(x - {x1})')

def plot_parallel_and_perpendicular_lines(m, b_parallel, b_perpendicular):
    x = np.linspace(-10, 10, 100)
    y_parallel = m * x + b_parallel
    y_perpendicular = (-1 / m) * x + b_perpendicular
    plt.plot(x, y_parallel, label=f'Parallel Line, y = {m}x + {b_parallel}')
    plt.plot(x, y_perpendicular, label=f'Perpendicular Line, y = {-1/m}x + {b_perpendicular}')

def plot_linear_inequality(A, B, C, inequality_type):
    x = np.linspace(-10, 10, 100)
    if inequality_type == '<=':
        y = (C - A * x) / B
        plt.fill_between(x, -10, y, color='gray', alpha=0.5, label=f'{A}x + {B}y <= {C}')
    elif inequality_type == '>=':
        y = (C - A * x) / B
        plt.fill_between(x, y, 10, color='gray', alpha=0.5, label=f'{A}x + {B}y >= {C}')
    else:
        print("Invalid inequality type. Use '<=' or '>='.")

def plot_piecewise_linear_functions(x_ranges, slopes, intercepts):
    for i in range(len(x_ranges)):
        x = np.linspace(x_ranges[i][0], x_ranges[i][1], 100)
        y = slopes[i] * x + intercepts[i]
        plt.plot(x, y, label=f'Piece {i + 1}: y = {slopes[i]}x + {intercepts[i]}')

# Add other plotting functions if needed

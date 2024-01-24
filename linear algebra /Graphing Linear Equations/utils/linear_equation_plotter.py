import matplotlib.pyplot as plt
import numpy as np

def plot_simple_linear_equation(A, B, C):
    x_values = np.linspace(-10, 10, 100)
    y_values = (C - A * x_values) / B

    plt.plot(x_values, y_values, label=f'{A}x + {B}y = {C}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Simple Linear Equation Plot')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_slope_intercept_form(m, b):
    x_values = np.linspace(-10, 10, 100)
    y_values = m * x_values + b

    plt.plot(x_values, y_values, label=f'y = {m}x + {b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Slope-Intercept Form Plot')
    plt.legend()
    plt.grid(True)
    plt.show()

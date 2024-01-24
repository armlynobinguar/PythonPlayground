# matrix_visualization_example.py
import numpy as np
import matplotlib.pyplot as plt

# Example matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Plotting the matrix
plt.imshow(matrix, cmap='viridis', interpolation='none')
plt.colorbar()
plt.title('Matrix Visualization')
plt.show()

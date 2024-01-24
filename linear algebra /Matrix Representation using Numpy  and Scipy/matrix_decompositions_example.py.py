# matrix_decompositions_example.py
import numpy as np
from scipy.linalg import lu, qr

# Example matrix
matrix = np.array([[1, 2], [3, 4]])

# LU decomposition
lu_result = lu(matrix)
lu_matrix = lu_result[0]
pivoting_matrix = lu_result[1]

# QR decomposition
qr_result = qr(matrix)
q_matrix = qr_result[0]
r_matrix = qr_result[1]

# Display the results
print("Example Matrix:")
print(matrix)
print(f"\nLU Decomposition:")
print("LU Matrix:")
print(lu_matrix)
print("Pivoting Matrix:")
print(pivoting_matrix)
print(f"\nQR Decomposition:")
print("Q Matrix:")
print(q_matrix)
print("R Matrix:")
print(r_matrix)

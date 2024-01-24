import numpy as np

# Example matrix for eigenvalue and eigenvector calculation
matrix = np.array([[4, -2], [1, 1]])

# Eigenvalue and eigenvector calculation
eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

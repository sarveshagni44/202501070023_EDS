#The given code takes two 3 x 3 matrices, matrix_a , and matrix_b , as input from the user and converts them into NumPy arrays.
#then perform certain mathematical operations on these matrices.

# code :

import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])



print("Addition (A + B):")
print(matrix_a + matrix_b)

print("Subtraction (A - B):")
print(matrix_a - matrix_b)

print("Element-wise Multiplication (A * B):")
print(matrix_a * matrix_b)

print("A dot B:")
print(matrix_a @ matrix_b)

print("Transpose of A:")
print(matrix_a.T)

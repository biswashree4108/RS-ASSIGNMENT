import numpy as np
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements:")
for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input())
        row.append(value)
    matrix.append(row)
a = np.array(matrix)
print("Matrix:")
print(a)
print("Shape:", a.shape)
print("Size:", a.size)
print("ndim:", a.ndim)
print("dtype:", a.dtype)
a = a.astype(float)               # Change datatype
print("After changing datatype:")
print(a)
print("New dtype:", a.dtype)
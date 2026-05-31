rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix1 = []
matrix2 = []
result = []
print("Enter elements of Matrix 1")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input())
        row.append(value)
    matrix1.append(row)
print("Enter elements of Matrix 2")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input())
        row.append(value)
    matrix2.append(row)

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
print("Result Matrix")
for row in result:
    print(row)
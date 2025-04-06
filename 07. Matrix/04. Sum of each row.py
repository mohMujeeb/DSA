mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


rows = len(mat)
columns = len(mat[0])

for i in range(rows):
    row_sum = 0
    for j in range(columns):
        row_sum += mat[i][j]
    print(f"Sum of row {i + 1}: {row_sum}")
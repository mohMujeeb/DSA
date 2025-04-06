mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

rows = len(mat)
columns = len(mat[0])

for i in range(columns):
    sum_col = 0
    for j in range(rows):
        sum_col += mat[j][i]
    print(f"Sum of column {i + 1}: {sum_col}")
    

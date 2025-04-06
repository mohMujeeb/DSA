mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

row = len(mat)
col = len(mat[0])

for i in range(col):
    for j in range(row):
        print(mat[j][i], end=" ")
    print()
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

rows = len(mat)
columns = len(mat[0])
total_sum = 0

for i in range(rows):
    for j in range(columns):
        total_sum += mat[i][j]


print("Total sum of matrix:", total_sum)

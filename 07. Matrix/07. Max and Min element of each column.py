mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

rows = len(mat)
cols = len(mat[0])

for i in range(cols):
    max_val = float('-inf')
    min_val = float('inf')
    for j in range(rows):
        if mat[j][i] > max_val:
            max_val = mat[j][i]
        if mat[j][i] < min_val:
            min_val = mat[j][i]
    print(f"Column {i}: Max = {max_val}, Min = {min_val}")
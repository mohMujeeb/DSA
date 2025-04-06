mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

rows = len(mat)
cols = len(mat[0])

for i in range(rows):
    max_ele = float('-inf')
    min_ele = float('inf')
    for j in range(cols):
        if mat[i][j] > max_ele:
            max_ele = mat[i][j]
        if mat[i][j] < min_ele:
            min_ele = mat[i][j]
    print(f"Row {i}: Max = {max_ele}, Min = {min_ele}")
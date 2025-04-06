def leftDiagonal(matrix, row, col):
    result = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if i == j:
                result[i][j] = matrix[i][j]
    return result

def rightDiagonal(matrix, row, col):
    result = [[0 for _ in range(col)] for _ in range(row)] 
    for i in range(row):
        for j in range(col):
            if i + j == row - 1:
                result[i][j] = matrix[i][j]
    return result

print("Upper Triangle Matrix:")
print(leftDiagonal([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]], 4, 4))
print("======================================================================")
print("Lower Triangle Matrix:")
print(rightDiagonal([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]], 4, 4))

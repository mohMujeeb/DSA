# Function to add two matrices
def add_matrices(matrix1, matrix2, rows, cols):
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    # Loop through each element of the matrices
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

# Function to subtract two matrices
def subtract_matrices(matrix1, matrix2, rows, cols):
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    # Loop through each element of the matrices
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result

# Hardcoded input matrices
matrix1 = [[1, 2, 3, 4], [6, 8, 7, 5], [9, 12, 11, 10]]
matrix2 = [[7, 3, 2, 1], [6, 9, 3, 12], [9, 23, 24, 11]]

# Perform operations
result_add = add_matrices(matrix1, matrix2, 3, 4)
result_sub = subtract_matrices(matrix1, matrix2, 3, 4)

# Print results
print(result_add)
print(result_sub)
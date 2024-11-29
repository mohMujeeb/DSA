def moveAllZeroToEnd(arr):
    n = len(arr)
    
    # create temp array 
    
    temp = [0] * n
    j = 0 
    
    # move non-zero elements to temp array
    for i in range(n):
        if arr[i]!=0:
            temp[j] = arr[i]
            j += 1
    
    # copy temp array to original array
    while j < n:
        temp[j] = 0
        j += 1
        
    # copy temp array to original array
    for i in range(n):
        arr[i] = temp[i]
        
    return arr

arr = [1, 2, 0, 4, 3, 0, 5, 0]

output = moveAllZeroToEnd(arr)
print(output)
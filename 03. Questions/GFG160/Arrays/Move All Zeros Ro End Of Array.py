""" 
Given an array arr[]. Push all the zeros of the given array to the right end 
of the array while maintaining the order of non-zero elements. Do the mentioned
change in the array in place.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
"""
# [Naive Approach] Using Temporary Array - O(n) Time and O(n) Space
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
# [Expected Approach] One Traversal - O(n) Time and O(1) Space

def pushZerosToEnd(arr):
    
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
            
    return arr

arr = [1, 2, 0, 4, 3, 0, 5, 0]

naive = moveAllZeroToEnd(arr)
expected = pushZerosToEnd(arr)


print(naive)
print(expected)
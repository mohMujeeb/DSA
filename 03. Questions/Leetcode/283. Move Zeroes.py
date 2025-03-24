""" 
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the 
non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
#Brute force approach
def brute(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
    for i in range(len(temp)):
        arr[i] = temp[i]
    nz = len(temp)
    for i in range(nz, n):
        arr[i] = 0
    return arr

def optimal(arr):
    j = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break
    
    if j == -1: return arr
    
    for i in range(j + 1, len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
            
    return arr


arr = [1, 2, 0, 4, 5, 0, 6, 0, 0, 8, 0]

print("Move Zero to end brute force:")
print(brute(arr))


print("Move Zero to end optimal:")
print(optimal(arr))
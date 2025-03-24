""" 
Given an array, arr. The task is to find the largest element in it.

Examples:

Input: arr = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
"""

# Brute force approach

def sortArray(arr):
    arr.sort()
    return arr[-1]

# Recursive approach
def largestElement(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [1, 8, 7, 56, 90]
print("Sort array method ")
print(sortArray(arr))

print("Recursive Method : ")
print(largestElement(arr))
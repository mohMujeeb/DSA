"""
Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d
is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples :

Input: arr[] = {1,2,3,4,5}, d = 2
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated by 2 elements, it becomes 3 4 5 1 2.
"""

def rotate(arr, d):
    n = len(arr)
    d = d % n
    
    l, r = 0, d - 1
    while l < n:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
        
    l, r = d, n - 1
    while l < n:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
        
    l, r = 0, n - 1
    while l < n:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
    







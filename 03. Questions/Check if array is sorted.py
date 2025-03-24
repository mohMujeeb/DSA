"""
Given an array of size n, write a program to check if the given array is sorted
in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted 
then return True, Else return False.

Examples
Example 1:
Input:
 N = 5, array[] = {1,2,3,4,5}
Output
    True
"""
def is_sorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

arr = [1, 2, 3, 4, 5]
n = len(arr)

print(is_sorted(arr, n))
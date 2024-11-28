"""Given an array of positive integers arr[], return the second largest element
from the array. If the second largest element doesn't exist then return -1.
Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest 
element is 34.
"""
def getSecondLargest(arr):
    n = len(arr)
    
    if n < 2:
        return -1
    
    large = -1 
    s_large = -1
    for i in range(n):
        if arr[i] > large:
            s_large = large
            large = arr[i]
        elif arr[i] > s_large and arr[i] < large:
            s_large = arr[i]
    return s_large    

arr = [12, 35, 1, 10, 34, 1]
second_largest = getSecondLargest(arr)  
print("Second largest element is:", second_largest)
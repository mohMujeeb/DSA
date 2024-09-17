"""
Given an array arr of size n−1 that contains distinct integers in the range of 1 to n (inclusive),
find the missing element. The array is a permutation of size n with one element missing. Return the
missing element.
Examples:

Input: n = 5, arr[] = [1,2,3,5]
Output: 4
Explanation : All the numbers from 1 to 5 are present except 4.
"""

def missingNumber(arr, n):
    
    hash_m = [0] * (n + 1)
    
    for num in arr:
        hash_m[num] += 1
    
    for i in range(1, n + 1):
        if hash_m[i] == 0:
            return i
        
    return -1

# Test the function
print(missingNumber([1, 2, 3, 5], 5))  # Output: 4

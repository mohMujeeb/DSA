#Given an array arr, return the second largest distinct element from an array.
#If the second largest element doesn't exist then return -1.
""" 
Time Complexity:
Brute force approach = O(N*logN)
Better Approach = O(N)
Optimal Approach = O(N) -> single pass solution
"""
# Brute force approach
def brute_force(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)
    arr.sort()
    s_largest = arr[-2]
    return s_largest
# Better approach
def better(arr, n):
    largest = arr[0]
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    sLargest = -1
    for i in range(n):
        if arr[i] > sLargest and arr[i] < largest:
            sLargest = arr[i]
    return sLargest


# Optimal Implementation
def optimal(arr, n):
    if (n < 2):
        return -1
    largest = float('-inf')
    second_largest = float('-inf')
    for i in range(n):
        if (arr[i] > largest):
            second_largest = largest
            largest = arr[i]
        elif (arr[i] > second_largest and arr[i] != largest):
            second_largest = arr[i]
    return second_largest


arr = [1, 2, 4, 6, 7, 5]
n = len(arr)

brute_force_approach = brute_force(arr, n)
print("Brute Force Approach: ", brute_force_approach)

better_approach = better(arr, n)
print("Better Approach: ", better_approach)

optimal_approach = optimal(arr, n)
print("Optimal Approach: ", optimal_approach)


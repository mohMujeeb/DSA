#Given an array arr, return the second small distinct element from an array.
#If the second small element doesn't exist then return -1.
""" 
Time Complexity:
Brute force approach = O(N*logN)
Better Approach = O(N)
Optimal Approach = O(N) -> single pass solution
"""

# Brute force approach

def brute_force(arr, n):
    if n == 0 and n == 1:
        return -1
    arr.sort()
    s_small = arr[1]
    return s_small

# Better approach 
def better_approach(arr, n):
    if n == 0 and n == 1:
        return -1
    small = arr[0]
    for i in range(n):
        if arr[i] < small:
            small = arr[i]
    s_small = float('inf')
    for i in range(n):
        if arr[i] < s_small and arr[i] != small:
            s_small = arr[i]
    return s_small

# Optimal approach
def optimal(arr, n):
    if n == 0 and n == 1:
        return -1
    small = float('inf')
    s_small = float('inf')
    for i in range(n):
        if arr[i] < small:
            s_small = small
            small = arr[i]
        elif arr[i] < s_small and arr[i] != small:
            s_small = arr[i]
    return s_small


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)

brute_force_approach = brute_force(arr, n)
print("Brute force approach:", brute_force_approach)

better_approach = better_approach(arr, n)
print("Better approach:", better_approach)

optimal_approach = optimal(arr, n)
print("Optimal approach:", optimal_approach) 

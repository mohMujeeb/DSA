""" 
Given an array of integers arr[] of size n, the task is to rotate the array 
elements to the left by d positions.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
Output: {3, 4, 5, 6, 1, 2}
Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and 
after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}
"""

#[Naive Approach] Rotate one by one - O(n * d) Time and O(1) Space

def naiveApproach(arr, d):
    n = len(arr)
    
    for i in range(d):
        
        first = arr[0]
        
        for j in range(n-1):
            arr[j] = arr[j + 1]
        
        arr[n - 1] = first
    
    return arr


arr = [1, 2, 3, 4, 5, 6]
d = 2

naive = naiveApproach(arr, d)

print("Naive Approach Output: ", naive) 


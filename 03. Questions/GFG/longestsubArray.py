


from typing import List
#Brute Force Approach
def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    length = 0
    for i in range(n): # starting index
        s = 0
        for j in range(i, n): # ending index
            # add the current element to the subarray a[i...j-1]:
            s += a[j]

            if s == k:
                length = max(length, j - i + 1)
    return length


a = [2, 3, 5, 1, 9]
k = 10
print("Brute force:")
print(getLongestSubarray(a, k))






from typing import List

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

if __name__ == '__main__':
    a = [2, 3, 5, 1, 9]
    k = 10
    len = getLongestSubarray(a, k)
    print("The length of the longest subarray is:", len)




def better_longest(arr, k):
    n = len(arr)
    maxLen = 0
    Sum = 0
    preSumMax = {}
    for i in range(n):
        Sum += arr[i]
        if Sum == k:
            maxLen= max(maxLen, i + 1)
            
        rem = Sum-k
        if rem in preSumMax:
            length = i - preSumMax[rem]
            maxLen = max(maxLen, length)
            
        if Sum not in preSumMax:
            preSumMax[Sum] = i
            
    return maxLen

a = [2, 3, 5, 1, 9]
k = 10
print("Longest Subarray with contigous length")
print(better_longest(a, k))



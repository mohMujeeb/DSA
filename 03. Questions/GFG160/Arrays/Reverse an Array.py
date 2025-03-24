# [Naive Approach] Using a temporary array - O(n) Time and O(n) Space

def naiveApproach(arr):
    n = len(arr)
    
    temp = [0] * n
    
    for i in range(n):
        temp[i] = arr[n - i - 1]
        
    for i in range(n):
        arr[i] = temp[i]
        
    return arr


# [Expected Approach ] Using Two Pointers - O(n) Time and O(1) Space

def expectedApproach(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr

arr = [1, 4, 3, 2, 6, 5]

naive = naiveApproach(arr)

expected = expectedApproach(arr)

print("Naive Approach Output: ", naive)
print("Expected Approach Output: ",expected)
#Given an array arr, return the second largest distinct element from an array.
#If the second largest element doesn't exist then return -1.
def secondLargest(arr, n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large





arr = [1, 2, 4, 7, 7, 5]
n = len(arr)
    
sL = secondLargest(arr, n)
print("Second largest is", sL)



def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return 
    
def permutations(res, arr, idx):
    # Base Case
    if idx == len(arr):
        res.append(arr[:])
        return
    
    for i in range(idx, len(arr)):
        swap(arr, idx, i)
        permutations(res, arr, idx+1)
        swap(arr, idx, i)
        
def permute(arr):
    res = []
    permutations(res, arr, 0)
    return res

arr = [1, 2, 3]
print(permute(arr))
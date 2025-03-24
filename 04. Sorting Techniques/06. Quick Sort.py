"""
QuickSort is a sorting algorithm based on the Divide and Conquer that picks
an element as a pivot and partitions the given array around the picked pivot
by placing the pivot in its correct position in the sorted array.

There are mainly three steps in the algorithm.
1. Choose a pivot
2. Partition the array around pivot. After partition, it is ensured that all elements are smaller than all right and we get index of the end point of smaller elements. The left and right may not be sorted individually.
3. Recursively call for the two partitioned left and right subarrays.
4. We stop recursion when there is only one element is left.

"""
# partition function 

def partition(arr, low, high):
    pivot = arr[low]
    
    i = low + 1
    j = high
    
    while i <= j:
        while arr[i] <= pivot and i <= high:
            i += 1
        while arr[j] > pivot and j >= low:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

# quicksort function

def quicksort(arr, low , high):
    if low < high:
        pi = partition(arr, low, high)
        
        quicksort(arr, low , pi - 1)
        quicksort(arr, pi + 1, high)
    return arr   
arr = [4, 6, 2, 5, 7, 9, 1, 3]
low = 0
high = len(arr)-1

print("Quick Sort: ")
quicksort(arr, low, high)
print(arr)
"""
Selection sort is a simple and efficient sorting algorithm that works by 
repeatedly selecting the smallest (or largest) element from the unsorted 
portion of the list and moving it to the sorted portion of the list.

Input = [4, 1, 3, 9, 7]
Output = [1, 3, 4, 7, 9]

Time complexity = O(N^2)
Space complexity = O(1) 
"""

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    return arr

arr = [4, 1, 3, 9, 7]
print(selection_sort(arr))   
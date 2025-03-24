"""
A sorting algorithm is said to be stable if two objects with equal or 
same keys appear in the same order in sorted output as they appear in
the input array to be sorted.

Selection sort can be made Stable if instead of swapping, the minimum 
element is placed in its position without swapping i.e. by placing the 
number in its position by pushing every element one step forward(shift 
all elements to left by 1). In simple terms use a technique like insertion
sort which means inserting element in its correct place. 

Time Complexity = O(n^2)
Auxiliary Complexity = O(1)
"""

def stable_selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        key = arr[min_idx]
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
        arr[i] = key
    return arr

arr = [4, 5, 3, 2, 4, 1]
print("Original array:", arr)
sorted_arr = stable_selection_sort(arr)
print("Sorted array:", sorted_arr)
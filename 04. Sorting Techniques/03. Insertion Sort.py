"""
Insertion sort is a simple sorting algorithm that works by iteratively 
inserting each element of an unsorted list into its correct position in a 
sorted portion of the list. It is a stable sorting algorithm, meaning that 
elements with equal values maintain their relative order in the sorted output.

Time Complexity: O(n^2)
Auxiliary Space: O(1)
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test the function
arr = [4, 2, 7, 1, 5, 3]
print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
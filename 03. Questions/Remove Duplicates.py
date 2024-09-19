"""
Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each
unique element appears only once. The relative order of the elements should be kept the same.If there
are k elements after removing the duplicates, then the first k elements of the array should hold the 
final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array.
"""
def removeDuplicates(arr):
    unique_list = []
    unique_dict = {}
    for value in arr:
        if value not in unique_dict:
            unique_dict[value] = True
            unique_list.append(value)
    return unique_list 

arr = [1, 1, 2, 2, 2, 3, 3]
print(removeDuplicates(arr))
"""
Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each
unique element appears only once. The relative order of the elements should be kept the same.
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
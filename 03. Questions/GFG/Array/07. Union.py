""" 
Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays
can be defined as the common and distinct elements in the two arrays. Return the elements in 
sorted order.
Example 1:

Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 5, arr2 [] = {1, 2, 3, 6, 7}
Output: 
1 2 3 4 5 6 7 
"""
# Brute force
def union(arr1, arr2, n, m):
    union_set = set()
    for i in range(n):
        union_set.add(arr1[i])
    for i in range(m):
        union_set.add(arr2[i])
    temp = []
    for num in union_set:
        temp.append(num)
    return temp

# Optimal Approach



def find_union(arr1, arr2, n, m):
    i, j = 0, 0  # Pointers
    union = []  # Union list

    while i < n and j < m:
        if arr1[i] <= arr2[j]:  # Case 1 and 2
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:  # Case 3
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < n:  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < m:  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]

n = len(arr1)
m = len(arr2)
# Brute Force
print(union(arr1, arr2, n, m))
# Optimal Approach
print(find_union(arr1, arr2, n, m))
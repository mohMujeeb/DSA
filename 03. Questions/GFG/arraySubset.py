"""
Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m, 
where both arrays may contain duplicate elements. The task is to
determine whether array a2 is a subset of array a1. It's important
to note that both arrays can be sorted or unsorted. Additionally, 
each occurrence of a duplicate element within an array is considered
as a separate element of the set.

Example 1:

Input:
a1[] = {11, 7, 1, 13, 21, 3, 7, 3}
a2[] = {11, 3, 7, 1, 7}
Output:
Yes 
"""

from collections import Counter

def is_subset(a1, a2):
    count_a1 = Counter(a1)
    count_a2 = Counter(a2)
    
    for element in a1:
        if count_a2[element] > count_a1.get(element, 0):
            return "No"
    return "Yes"

# Test the function
a1 = [11, 7, 1, 13, 21, 3, 7, 3]
a2 = [11, 3, 7, 1, 7]
print(is_subset(a1, a2))
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that 
the majority element always exists in the array.
Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
#Brute force TC-> O(n^2).
def majority(arr):
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                cnt += 1
    
        if cnt > len(arr)//2:
            return arr[i]
# Better Approach TC-> O(n).
from collections import Counter
def majority_count(arr):
    counter = Counter(arr)
    for num, count in counter.items():
        if count > len(arr) // 2:
            return num
    return -1

# Optimal approach
# Moore's Voting Algorithm TC-> O(n)
def moor_vote(arr):
    vote = 0
    candidate = -1
    
    for i in range(len(arr)):
        if vote == 0:
            candidate = arr[i]
            vote = 1
        else:
            if candidate == arr[i]:
                vote+=1
            else:
                vote -= 1
    count = 0
    for i in range(len(arr)):
        if arr[i] == candidate:
            count += 1
    
    if count > len(arr) // 2:
        return candidate
    else: 
        return -1
    
        

test_case1 = [2, 2, 3, 3, 1, 2,2]    
test_case2 = [ 1, 1, 1, 1, 2, 3, 4 ]
# Brute force
print("Brute force")
print(majority(test_case1))
print(majority(test_case2))
# Better approach
print("Better approach")
print(majority_count(test_case1))
print(majority_count(test_case2))
# Optimal approach
print("Optimal approach")
print(moor_vote(test_case1))
print(moor_vote(test_case2))


"""
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.You may assume that each input 
would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

# Brute Force Method

def twoSum_bruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
#Time Complexity: O(n^2)
            
# Optimized Method using Hash Table

def twoSum_hash(nums, target):
    map = {} # Value : Index
    for ind, val in enumerate(nums):
        diff = target - val
        if diff in map:
            return [map[diff], ind]
        map[val] = ind
    return

# Time Complexity: O(n)

# Test Cases
nums = [2,7,11,15]
target = 9

print("Brute Force Method Output: ")
print(twoSum_bruteForce(nums, target))

print("Hash Table Method Output: ")
print(twoSum_hash(nums, target))
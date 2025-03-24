""" 
Given an integer array nums, rotate the array to the right by k steps, 
where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

def rotate_array(nums, k):
    k = k % len(nums)
    
    l, r = 0, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r -1
        
    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    
    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    return nums
nums = [1, 2, 3, 4, 5, 6]
k = 2

print("Rotated Array:")
print(rotate_array(nums, k))
""" 
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""
def findMacConsecutiveOnes(nums):
    n = len(nums)
    cnt = 0
    maxi = 0
    
    for i in range(n):
        if nums[i] == 1:
            cnt += 1
            maxi = max(maxi, cnt)
        else:
            cnt = 0
    
    return maxi


nums1 = [1,1,0,1,1,1]
nums2 = [1,0,1,1,0,1]

print(findMacConsecutiveOnes(nums1)) # Output: 3
print(findMacConsecutiveOnes(nums2)) # Output: 2
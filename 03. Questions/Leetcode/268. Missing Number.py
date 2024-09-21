""" 
Given an array nums containing n distinct numbers in the range [0, n], return the only number
in the range that is missing from the array.
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the 
missing number in the range since it does not appear in nums.
"""
# Better Approach
def missingNumber(nums):
    n = len(nums)
    h_map = [0] * (n + 1)
    
    for num in nums:
        h_map[num] += 1
    
    for i in range(n + 1):
        if h_map[i] == 0:
            return i
    return -1

# Optimal Approach
def optimal(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    # actual_sum
    actual_sum = 0 
    for i in range(n):
        actual_sum += nums[i]
        
    return expected_sum - actual_sum
        
#XOR Approach
def xor(nums):
    n = len(nums)
    xor1 = 0 
    xor2 = 0
    for i in range(n):
        xor1 = xor1 ^ nums[i]
        xor2 = xor2 ^ i
    xor2 = xor2 ^ n
    return xor1 ^ xor2
#Better approach
nums = [3, 0, 1]
print("Brute Force")
print(missingNumber(nums))  # Output: 2
#Optimal approach
print("Optimal approach")
print(optimal(nums))  # Output: 2
# XOR Approach
print("XOR approach")
print(xor(nums))
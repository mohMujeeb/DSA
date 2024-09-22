"""Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.You must implement a solution with a linear runtime complexity and 
use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Brute force Time Complexity: O(n^2)
Better Time Complexity: O(N*logM) + O(M)
Optimal Time Complexity: O(N)
"""

# Brute force approach  
def bruteForce(nums):
    n = len(nums)
    for i in range(n):
        num = nums[i]
        cnt = 0
        for j in range(n):
            if nums[j] == num:
                cnt += 1
        if cnt == 1:
            return num

# Better approach
def better(nums):
    n = len(nums)
    
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1
    
    for num, count in hashmap.items():
        if count == 1:
            return num


# Optimal approach
def optimal(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor      
nums = [4,1,2,1,2]  
# Brute force approach
print("Brute force approach")
print(bruteForce(nums))

# Better approach
print("Better approach")
print(bruteForce(nums))

# Optimal Approach
print("Optimal Approach")
print(optimal(nums))


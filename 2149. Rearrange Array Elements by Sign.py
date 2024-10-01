"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative 
integers.You should return the array of nums such that the the array follows the given conditions:

-> Every consecutive pair of integers have opposite signs.
-> For all integers with the same sign, the order in which they were present in nums is preserved.
-> The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
"""

# Brute Force Approach  TC -> O(n + n/2)
def rearrangeArray(nums):
    pos = []
    neg = []
    
    for i in range(len(nums)):
        if nums[i] > 0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
            
    for i in range(len(pos)):
        nums[i * 2] = pos[i]
    for i in range(len(neg)):
        nums[i * 2 + 1] = neg[i]
        
    return nums

# Optimized Approach TC -> O(N)

def rearrangeArray2(nums):
    n = len(nums)
    ans = [0] * n
    
    posInd, negInd = 0, 1
    
    for num in nums:
        if num > 0:
            ans[posInd] = num
            posInd += 2
        else:
            ans[negInd] = num
            negInd += 2
    return ans

nums = [3,1,-2,-5,2,-4]
print("Brute Force")
print(rearrangeArray(nums))

print("Optimal Approach")
print(rearrangeArray2(nums))
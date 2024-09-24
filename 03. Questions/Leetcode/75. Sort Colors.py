""" 
Given an array nums with n objects colored red, white, or blue, sort them in-place so that 
objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Solved using Dutch National Flag Algorithm 
"""
def sortColors(nums):
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low, mid = low+1, mid+1
            elif nums[mid] == 1:
                mid = mid+1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high = high - 1
        return nums

            
test_case1 = [2, 0, 2, 1, 1, 0]
test_case2 = [2, 0, 1]
print("Sorted Colors:")
print("For Test Case 1:")
print(sortColors(test_case1))
print("For Test Case 2:")
print(sortColors(test_case2))

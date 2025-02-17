class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        count = 0 

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[count] = nums[count], nums[i]

                count += 1
        return nums
        
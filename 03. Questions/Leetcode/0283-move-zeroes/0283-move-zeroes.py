class Solution(object):
    def moveZeroes(self, nums):
        """for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
        return nums"""

        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        if j == -1: return nums
        for i in range(j+1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            
        return nums

        
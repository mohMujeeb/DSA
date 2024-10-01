class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        ans = [0] * n

        posInd, negInd = 0, 1

        for i in range(n):
            if nums[i] < 0:
                ans[negInd] = nums[i]
                negInd += 2
            else:
                ans[posInd] = nums[i]
                posInd += 2
        return ans

        
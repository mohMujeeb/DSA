class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)

        Sum = 0
        Maxi = nums[0]

        for i in range(n):
            Sum += nums[i]

            Maxi = max(Maxi, Sum)
            
            if Sum < 0:
                Sum = 0
        return Maxi
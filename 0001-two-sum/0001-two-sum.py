class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h_map = {}
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in h_map:
                return [h_map[diff], ind]
            h_map[val] = ind
        return 

        
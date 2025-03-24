class Solution(object):
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    
    def permutations(self, res, nums, idx):
        if idx == len(nums):
            res.append(nums[:])  # Append a copy of the current permutation
            return 
        for i in range(idx, len(nums)):
            self.swap(nums, idx, i)
            self.permutations(res, nums, idx + 1)
            self.swap(nums, idx, i)  # Backtrack

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.permutations(res, nums, 0)  # Use self to call the method
        return res

        
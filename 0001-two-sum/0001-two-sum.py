class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        f = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in f:
                return f[diff], i
            f[n] = i
        return
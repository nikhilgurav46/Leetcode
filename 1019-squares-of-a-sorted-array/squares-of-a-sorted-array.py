class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        i = 0
        j = len(nums) - 1

        while (i <= j):
            if nums[i] * nums[i] < nums[j] * nums[j]:
                res.append(nums[j] * nums[j])
                j -= 1

            else:
                res.append(nums[i] * nums[i])
                i += 1

        return res[::-1]
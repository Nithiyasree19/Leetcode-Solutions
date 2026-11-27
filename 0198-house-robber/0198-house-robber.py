class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = curr = 0
        for n in nums:
            prev, curr = curr, max(curr, prev + n)
        return curr
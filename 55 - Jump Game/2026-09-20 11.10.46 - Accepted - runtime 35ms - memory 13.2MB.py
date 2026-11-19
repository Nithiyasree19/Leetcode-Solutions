class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0

        for i, jump in enumerate(nums):
            if i > farthest:
                return False

            farthest = max(farthest, i + jump)

            if farthest >= len(nums) - 1:
                return True

        return True
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for current in range(target, num - 1, -1):
                dp[current] = dp[current] or dp[current - num]

        return dp[target]
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []

        for num in nums:
            i = bisect_left(tails, num)

            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num

        return len(tails)
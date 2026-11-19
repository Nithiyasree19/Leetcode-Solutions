class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix = 0
        freq = {0: 1}
        for num in nums:
            prefix += num
            count += freq.get(prefix - k, 0)
            freq[prefix] = freq.get(prefix, 0) + 1
        return count
        
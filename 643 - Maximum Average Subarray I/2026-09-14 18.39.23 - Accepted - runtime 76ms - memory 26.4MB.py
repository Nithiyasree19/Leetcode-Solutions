class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for incoming, outgoing in zip(nums[k:], nums):
            current_sum += incoming - outgoing
            if current_sum > max_sum:
                max_sum = current_sum
                
        return float(max_sum) / k
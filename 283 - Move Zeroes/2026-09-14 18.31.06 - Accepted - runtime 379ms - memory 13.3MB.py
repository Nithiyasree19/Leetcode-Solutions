class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        if zero_count == 0 or zero_count == len(nums):
            return
        for _ in range(zero_count):
            nums.remove(0)
        nums.extend([0] * zero_count)
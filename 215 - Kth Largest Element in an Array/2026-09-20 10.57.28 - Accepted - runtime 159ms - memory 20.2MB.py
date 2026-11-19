import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]

            low = left
            mid = left
            high = right

            while mid <= high:
                if nums[mid] < pivot:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1
                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
                else:
                    mid += 1

            if target < low:
                right = low - 1
            elif target > high:
                left = high + 1
            else:
                return nums[target]
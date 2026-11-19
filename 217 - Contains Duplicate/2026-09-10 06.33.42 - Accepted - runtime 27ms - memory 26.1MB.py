class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()       
        for i in nums:
            if i in seen:
                return True
                Break
            else:
                seen.add(i)
        else:
            return False

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        tot=0
        for i in nums:
            tot+=i
            result.append(tot)
        return result
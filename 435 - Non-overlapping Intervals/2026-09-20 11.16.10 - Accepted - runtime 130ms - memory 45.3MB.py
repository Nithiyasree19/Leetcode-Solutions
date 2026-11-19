class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])

        removed = 0
        end = float("-inf")

        for start, finish in intervals:
            if start < end:
                removed += 1
            else:
                end = finish

        return removed
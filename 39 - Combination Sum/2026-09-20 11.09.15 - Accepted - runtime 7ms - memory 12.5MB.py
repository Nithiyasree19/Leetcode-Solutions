class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        combination = []

        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(combination[:])
                return

            for i in range(start, len(candidates)):
                coin = candidates[i]

                if coin > remaining:
                    break

                combination.append(coin)
                backtrack(i, remaining - coin)
                combination.pop()

        backtrack(0, target)
        return result
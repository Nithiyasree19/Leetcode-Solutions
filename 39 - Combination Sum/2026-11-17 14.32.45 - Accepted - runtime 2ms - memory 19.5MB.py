class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
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
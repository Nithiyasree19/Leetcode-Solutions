class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)

        if n < d:
            return -1

        INF = float("inf")

        # dp[i] = minimum difficulty for scheduling the first i jobs
        # using the current number of days.
        dp = [INF] * (n + 1)
        dp[0] = 0

        for day in range(1, d + 1):
            next_dp = [INF] * (n + 1)

            # Need at least 'day' jobs for 'day' days
            for i in range(day, n + 1):
                hardest = 0

                # Last day handles jobs j ... i-1
                for j in range(i - 1, day - 2, -1):
                    hardest = max(hardest, jobDifficulty[j])

                    if dp[j] != INF:
                        next_dp[i] = min(
                            next_dp[i],
                            dp[j] + hardest
                        )

            dp = next_dp

        return dp[n]
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        prev = list(range(len(word2) + 1))

        for i in range(1, len(word1) + 1):
            curr = [i] + [0] * len(word2)

            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(
                        prev[j],      # Delete
                        curr[j - 1],  # Insert
                        prev[j - 1]   # Replace
                    )

            prev = curr

        return prev[-1]
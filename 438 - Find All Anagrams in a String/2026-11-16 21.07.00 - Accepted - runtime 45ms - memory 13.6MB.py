from collections import Counter as c
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []

        count = [0] * 26

        for char in p:
            count[ord(char) - 97] += 1

        result = []
        left = 0
        k = len(p)

        for right in range(len(s)):
            count[ord(s[right]) - 97] -= 1

            if right - left + 1 > k:
                count[ord(s[left]) - 97] += 1
                left += 1

            if right - left + 1 == k and not any(count):
                result.append(left)

        return result
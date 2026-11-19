from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        need = Counter(t)
        have = {}
        required = len(need)
        formed = 0

        left = 0
        best_len = float("inf")
        best_left = 0

        for right, char in enumerate(s):
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while formed == required:
                window_len = right - left + 1

                if window_len < best_len:
                    best_len = window_len
                    best_left = left

                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_left:best_left + best_len]
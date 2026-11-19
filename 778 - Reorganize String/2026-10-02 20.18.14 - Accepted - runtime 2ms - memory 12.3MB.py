import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s):
        count = Counter(s)

        # Impossible if one character appears too many times
        if max(count.values()) > (len(s) + 1) // 2:
            return ""

        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        result = []
        prev_freq = 0
        prev_char = ""

        while heap:
            freq, char = heapq.heappop(heap)

            result.append(char)

            # Put the previous character back after using another character
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            freq += 1
            prev_freq = freq
            prev_char = char

        return "".join(result)
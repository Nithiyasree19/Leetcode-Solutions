class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        words.discard(beginWord)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            chars = list(word)

            for i in range(len(chars)):
                original = chars[i]

                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original:
                        continue

                    chars[i] = c
                    next_word = "".join(chars)

                    if next_word in words:
                        words.remove(next_word)
                        queue.append((next_word, steps + 1))

                chars[i] = original

        return 0
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return

            next_node = node.children[char]

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None

            board[r][c] = '#'

            if r > 0 and board[r - 1][c] != '#':
                dfs(r - 1, c, next_node)

            if r + 1 < rows and board[r + 1][c] != '#':
                dfs(r + 1, c, next_node)

            if c > 0 and board[r][c - 1] != '#':
                dfs(r, c - 1, next_node)

            if c + 1 < cols and board[r][c + 1] != '#':
                dfs(r, c + 1, next_node)

            board[r][c] = char

            # Prune unused Trie branches
            if not next_node.children and next_node.word is None:
                del node.children[char]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result
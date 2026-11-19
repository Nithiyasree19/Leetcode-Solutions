class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(heights)
        cols = len(heights[0])

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()

                for nr, nc in ((r + 1, c), (r - 1, c),
                               (r, c + 1), (r, c - 1)):
                    if (nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        (nr, nc) in visited):
                        continue

                    if heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return visited

        pacific = []
        atlantic = []

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        pacific = bfs(pacific)
        atlantic = bfs(atlantic)

        return [[r, c] for r, c in pacific & atlantic]
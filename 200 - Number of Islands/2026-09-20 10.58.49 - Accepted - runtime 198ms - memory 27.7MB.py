class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    stack = [(r, c)]
                    grid[r][c] = "0"

                    while stack:
                        x, y = stack.pop()

                        if x > 0 and grid[x - 1][y] == "1":
                            grid[x - 1][y] = "0"
                            stack.append((x - 1, y))

                        if x + 1 < rows and grid[x + 1][y] == "1":
                            grid[x + 1][y] = "0"
                            stack.append((x + 1, y))

                        if y > 0 and grid[x][y - 1] == "1":
                            grid[x][y - 1] = "0"
                            stack.append((x, y - 1))

                        if y + 1 < cols and grid[x][y + 1] == "1":
                            grid[x][y + 1] = "0"
                            stack.append((x, y + 1))

        return islands
        
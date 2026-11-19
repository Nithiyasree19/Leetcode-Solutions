class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        min_dist = [float("inf")] * n
        min_dist[0] = 0

        visited = [False] * n
        total = 0

        for _ in range(n):
            curr = -1

            # Find unvisited point with minimum connection cost
            for i in range(n):
                if not visited[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i

            visited[curr] = True
            total += min_dist[curr]

            x1, y1 = points[curr]

            # Update costs for remaining points
            for i in range(n):
                if not visited[i]:
                    x2, y2 = points[i]
                    distance = abs(x1 - x2) + abs(y1 - y2)

                    if distance < min_dist[i]:
                        min_dist[i] = distance

        return total
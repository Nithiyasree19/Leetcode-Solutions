class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            if time != dist[node]:
                continue

            for nei, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))

        result = max(dist[1:])

        return -1 if result == float("inf") else result
        
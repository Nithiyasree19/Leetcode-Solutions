class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        left = 0
        right = len(points) - 1

        def distance(i):
            x, y = points[i]
            return x * x + y * y

        while left <= right:
            pivot = distance((left + right) // 2)

            i = left
            j = right

            while i <= j:
                while distance(i) < pivot:
                    i += 1

                while distance(j) > pivot:
                    j -= 1

                if i <= j:
                    points[i], points[j] = points[j], points[i]
                    i += 1
                    j -= 1

            if k - 1 <= j:
                right = j
            elif k - 1 >= i:
                left = i
            else:
                break

        return points[:k]
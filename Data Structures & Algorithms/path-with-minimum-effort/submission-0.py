class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, (0, 0))]
        visited = set()
        n = len(heights)
        m = len(heights[0])

        while heap:
            weight, node = heapq.heappop(heap)
            nodeX, nodeY = node
            if node in visited:
                continue
            visited.add(node)

            if nodeX == n - 1 and nodeY == m - 1:
                return weight

            if nodeX > 0:
                heightDiff = abs(heights[nodeX][nodeY] - heights[nodeX - 1][nodeY])
                heapq.heappush(heap, (max(weight, heightDiff), (nodeX - 1, nodeY)))
            if nodeX < n - 1:
                heightDiff = abs(heights[nodeX][nodeY] - heights[nodeX + 1][nodeY])
                heapq.heappush(heap, (max(weight, heightDiff), (nodeX + 1, nodeY)))
            if nodeY > 0:
                heightDiff = abs(heights[nodeX][nodeY] - heights[nodeX][nodeY - 1])
                heapq.heappush(heap, (max(weight, heightDiff), (nodeX, nodeY - 1)))
            if nodeY < m - 1:
                heightDiff = abs(heights[nodeX][nodeY] - heights[nodeX][nodeY + 1])
                heapq.heappush(heap, (max(weight, heightDiff), (nodeX, nodeY + 1)))

        return -1

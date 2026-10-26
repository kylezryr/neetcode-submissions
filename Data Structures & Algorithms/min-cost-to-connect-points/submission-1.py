class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim's algorithm for MSTs

        n = len(points)
        currNode = 0
        dist = [10000000] * n
        visited = [False] * n
        edgeCount = 0
        result = 0

        while edgeCount < n - 1:
            visited[currNode] = True
            nextNode = -1
            for i in range(n):
                if visited[i]:
                    continue
                currDist = (abs(points[i][0] - points[currNode][0]) + 
                        abs(points[i][1] - points[currNode][1]))
                dist[i] = min(dist[i], currDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            result += dist[nextNode]
            currNode = nextNode
            edgeCount += 1

        return result

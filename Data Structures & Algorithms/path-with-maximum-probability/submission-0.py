class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        visited = set()
        adjList = {i: [] for i in range(n)}

        for i in range(len(edges)):
            source = edges[i][0]
            dest = edges[i][1]
            weight = succProb[i]
            adjList[source].append((dest, -weight))
            adjList[dest].append((source, -weight))

        heap = [(-1.0, start_node)]
        while heap:
            prob, node = heapq.heappop(heap)

            if node == end_node:
                return -prob

            visited.add(node)
            for neighbor, neighborProb in adjList[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (-(prob * neighborProb), neighbor))
            
        return 0
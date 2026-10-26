class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build adjList
        adjList = {i: [] for i in range(n)}
        for source, dest, weight in flights:
            adjList[source].append((dest, weight))
        
        heap = [(0, src, 0)]
        visited = set()

        while heap:
            weight, node, stops = heapq.heappop(heap)
            
            if (node, stops) in visited:
                continue
            
            if node == dst:
                return weight

            visited.add((node, stops))

            if stops > k:
                continue

            for dest, destWeight in adjList[node]:
                heapq.heappush(heap, (weight + destWeight, dest, stops + 1))

        return -1
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        visited = set()
        time = 0

        # build adjList
        adjList = collections.defaultdict(list)
        for time in times:
            source = time[0]
            target = time[1]
            travelTime = time[2]
            adjList[source].append((target, travelTime))

        # visit nodes in shortest path order
        while heap:
            travelTime, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            time = travelTime

            for neighborNode, neighborTravelTime in adjList[node]:
                if neighborNode not in visited:
                    heapq.heappush(heap, (travelTime + neighborTravelTime, neighborNode))

        return time if len(visited) == n else -1

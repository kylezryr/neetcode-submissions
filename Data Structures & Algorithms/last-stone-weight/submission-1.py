class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        
        for stone in stones:
            heapq.heappush_max(maxHeap, stone)

        while len(maxHeap) > 1:
            larger = heapq.heappop_max(maxHeap)
            smaller = heapq.heappop_max(maxHeap)

            if larger != smaller:
                heapq.heappush_max(maxHeap, larger - smaller)

        if len(maxHeap) == 0:
            return 0 

        return heapq.heappop_max(maxHeap)
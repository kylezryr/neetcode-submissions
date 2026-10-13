class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.min_heap_len = 0
        self.max_heap_len = 0

    def addNum(self, num: int) -> None:
        min_heap_min = self.min_heap[0] if self.min_heap else 0
        max_heap_max = self.max_heap[0] if self.max_heap else 0

        if num > min_heap_min:
            heapq.heappush(self.min_heap, num)
            self.min_heap_len += 1
        else:
            heapq.heappush(self.max_heap, -num)
            self.max_heap_len += 1

        if abs(self.min_heap_len - self.max_heap_len) > 1:
            if self.min_heap_len > self.max_heap_len:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                self.min_heap_len -= 1
                self.max_heap_len += 1
            else:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                self.max_heap_len -= 1
                self.min_heap_len += 1

    def findMedian(self) -> float:
        if self.min_heap_len == self.max_heap_len:
            return (self.min_heap[0] + -self.max_heap[0])/2
        elif self.min_heap_len > self.max_heap_len:
            return self.min_heap[0]
        else:
            return -self.max_heap[0]

        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        result = []
        
        # sort list
        intervals.sort(key=lambda x: x[0])
        currentInterval = intervals[0]

        for i in range(1, len(intervals)):
            nextInterval = intervals[i]
            # join intervals if start of second <= end of first
            if nextInterval[0] <= currentInterval[1]:
                currentInterval[1] = max(nextInterval[1], currentInterval[1])
            else:
                result.append(currentInterval)
                currentInterval = nextInterval

        result.append(currentInterval)
        
        return result

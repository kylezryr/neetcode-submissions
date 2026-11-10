class TimeMap:

    def __init__(self):
        self.kvMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kvMap:
            self.kvMap[key].append((timestamp, value))
        else:
            self.kvMap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvMap:
            return ""
        
        # binary search on values for key
        valuesList = self.kvMap[key]
        left = 0 
        right = len(valuesList) - 1
        prev = ""

        while left <= right:
            middle = (left + right) // 2
            middleTimestamp, middleValue = valuesList[middle]
            if timestamp == middleTimestamp:
                return middleValue
            elif middleTimestamp < timestamp:
                prev = middleValue
                left = middle + 1
            else:
                right = middle - 1

        return prev


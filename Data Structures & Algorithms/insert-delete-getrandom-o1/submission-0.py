class RandomizedSet:

    def __init__(self):
        self.numToIndex = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.numToIndex:
            return False
        self.numToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numToIndex:
            return False
        index = self.numToIndex[val]
        elemAtEnd = self.nums[-1]
        elemAtEndIndex = self.numToIndex[elemAtEnd]
        self.numToIndex[elemAtEnd] = index
        self.nums[index] = elemAtEnd
        self.nums.pop()
        self.numToIndex.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
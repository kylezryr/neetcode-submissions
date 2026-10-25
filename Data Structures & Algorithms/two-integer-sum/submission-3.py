class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            numToIndex[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target-nums[i]
            if (diff) in numToIndex and i != numToIndex[diff]:
                return [i, numToIndex[diff]] 

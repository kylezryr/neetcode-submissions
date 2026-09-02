class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqCount = {}
        majoritySize = len(nums) // 2

        for num in nums:
            freqCount[num] = 1 + freqCount.get(num, 0)
            if freqCount[num] > majoritySize:
                return num

        return -1
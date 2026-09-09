class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        best = 0
        current = 0

        while i < n:
            if nums[i] == 1:
                current += 1
                best = max(best, current)
            else:
                current = 0
            i += 1

        return best
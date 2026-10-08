class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dpFirst = [0] * (n-1)
        dpFirst[0] = nums[0]
        dpFirst[1] = max(nums[0], nums[1])
        dpLast = [0] * (n-1)
        dpLast[0] = nums[1]
        dpLast[1] = max(nums[1], nums[2])

        # first pass including first house, excluding last house
        for i in range(2, n-1):
            dpFirst[i] = max(nums[i] + dpFirst[i-2], dpFirst[i-1])
        
        # second pass excluding first house, including last house
        numsExcluded = nums[1:]
        for i in range(2, n-1):
            dpLast[i] = max(numsExcluded[i] + dpLast[i-2], dpLast[i-1])

        return max(dpFirst[-1], dpLast[-1])
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currMin = 1
        currMax = 1

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            product = currMax * nums[i]
            currMax = max(nums[i] * currMax, nums[i] * currMin, nums[i])
            currMin = min(product, nums[i] * currMin, nums[i])
            result = max(result, currMax)

        return result
            
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            # either add current element to sum
            # or start fresh
            currSum = max(currSum + nums[i], nums[i])

            # update result if larger
            result = max(result, currSum)

        return result

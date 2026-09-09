class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        # scan from the right to find the first smaller elem
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # find first element to the right greater than i
        if i >= 0:
            j = n-1 
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse subarray from i+1 to the end
        l = i + 1
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
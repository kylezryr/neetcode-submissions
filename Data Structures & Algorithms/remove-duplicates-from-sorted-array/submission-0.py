class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 0

        while right < len(nums):
            nums[left] = nums[right]
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            left += 1
        
        return left
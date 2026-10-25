class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum == 0:
                    triplet = [nums[left], nums[right], nums[i]]
                    if triplet not in result:
                        result.append(triplet)
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        return result
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for p1 in range(n):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            for p2 in range(p1 + 1, n):
                if p2 > p1 + 1 and nums[p2] == nums[p2-1]:
                    continue
                left = p2 + 1
                right = n - 1
                while left < right:
                    sum = nums[p1] + nums[p2] + nums[left] + nums[right]

                    if sum == target:
                        quad = [nums[p1], nums[p2], nums[left], nums[right]]
                        result.append(quad)
                        left += 1
                        right -= 1
                        # skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif sum < target:
                        left += 1
                    
                    elif sum > target:
                        right -= 1

        return result
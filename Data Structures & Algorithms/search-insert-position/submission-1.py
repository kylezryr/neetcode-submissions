class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        left = 0
        n = len(nums)
        right = n - 1
        result = n

        while left <= right:
            middle = (left + right) // 2
            current = nums[middle]

            if current == target:
                return middle
            elif current < target:
                left = middle + 1
            else:
                result = middle
                right = middle - 1

        return result
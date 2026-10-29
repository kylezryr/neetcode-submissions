class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            middle = (left + right) // 2
            leftNeighbor = nums[middle - 1] if middle > 0 else -math.inf
            rightNeighbor = nums[middle + 1] if middle < n - 1 else -math.inf

            if nums[middle] > leftNeighbor and nums[middle] > rightNeighbor:
                return middle
            elif nums[middle] < leftNeighbor:
                right = middle - 1
            else:
                left = middle + 1

        return -1
            
            
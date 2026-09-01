class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer approach
        left = 0
        right = len(heights) - 1
        maxHeight = -1

        while left < right:
            volume = (right - left) * min(heights[left], heights[right])

            if volume > maxHeight:
                maxHeight = volume
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxHeight
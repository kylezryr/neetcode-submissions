class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        result = 0

        while left <= right:
            middle = left + (right - left) // 2
            product = middle * middle

            if product > x:
                right = middle - 1
            elif product < x:
                left = middle + 1
                result = middle
            else:
                return middle

        return result
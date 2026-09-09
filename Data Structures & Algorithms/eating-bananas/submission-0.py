class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            speed = (left + right) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / speed)
            if totalTime <= h:
                result = speed
                right = speed - 1
            else:
                left = speed + 1

        return result
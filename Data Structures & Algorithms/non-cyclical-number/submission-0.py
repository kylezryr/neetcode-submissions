class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        while n != 1:
            squares = [int(digit) ** 2 for digit in str(n)]
            sumSquares = sum(squares)
            if sumSquares in seen:
                return False
            seen.add(sumSquares)
            n = sumSquares

        return True
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MAX_INT = (1 << 31) - 1 # max 32 bit integer
        MIN_INT = -(1 << 31)
        negate = False

        if x < 0:
            negate = True
            x = -x

        limit = -MIN_INT if negate else MAX_INT

        while x > 0:
            digit = x % 10
            if res > limit // 10:
                return 0
            elif res == limit // 10 and digit > limit % 10:
                return 0

            res = (res * 10) + digit
            x = x//10
            
        if negate:
            res = -res

        return res
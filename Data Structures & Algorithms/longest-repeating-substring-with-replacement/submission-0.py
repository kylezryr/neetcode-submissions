class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 1:
            return 0

        charSet = set(s)
        n = len(s)
        best = 0

        for c in charSet:
            left = 0
            count = 0
            for r in range(n):
                if s[r] == c:
                    count += 1
                
                # size of window = r - left + 1
                # while the size of the window - freq of c is more than k,
                # move left until we can use k replacements
                while (r - left + 1) - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1

                best = max(best, r - left + 1)
            
        return best
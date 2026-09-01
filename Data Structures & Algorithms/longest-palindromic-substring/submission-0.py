class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(start: int, end:int):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            
            return end - start - 1
        
        start = end = 0

        for i in range(len(s)):
            oddLength = expandFromCenter(i, i)
            evenLength = expandFromCenter(i, i+1)
            bestLength = max(oddLength, evenLength)

            if bestLength > end - start + 1:
                start = i - (bestLength - 1)//2
                end = i + bestLength//2

        return s[start:end+1]
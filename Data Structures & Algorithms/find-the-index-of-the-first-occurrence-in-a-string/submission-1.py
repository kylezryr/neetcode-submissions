class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for left in range(n - m + 1):
            right = 0
            while (right < m):
                if haystack[left + right] != needle[right]:
                    break
                right += 1
            if right == m:
                return left
    
        return -1            

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        letters = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            
            letters.add(s[right])
            length = right - left + 1
            if length > maxLength:
                maxLength = length

        return maxLength

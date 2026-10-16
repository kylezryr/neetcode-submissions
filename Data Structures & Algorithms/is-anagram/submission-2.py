class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreqCount = {}
        tFreqCount = {}

        for c in s:
            sFreqCount[c] = sFreqCount.get(c, 0) + 1

        for c in t:
            tFreqCount[c] = tFreqCount.get(c, 0) + 1

        return sFreqCount == tFreqCount
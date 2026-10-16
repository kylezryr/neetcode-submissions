class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqCountToWords = {}
        
        for word in strs:
            freqCount = [0] * 26
            for c in word: 
                charIndex = ord(c) - ord('a')
                freqCount[charIndex] = freqCount[charIndex] + 1
            
            if tuple(freqCount) in freqCountToWords:
                freqCountToWords[tuple(freqCount)].append(word)
            else:
                freqCountToWords[tuple(freqCount)] = [word]
        
        return list(freqCountToWords.values())
            
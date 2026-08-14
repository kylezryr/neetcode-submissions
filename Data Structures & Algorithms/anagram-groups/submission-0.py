class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            freqCount = [0] * 26 # 26-length array for frequency of each alphabet
            for c in string:
                charIndex = ord(c) - ord('a') # converts character into 0-26 index
                freqCount[charIndex] += 1
            result[tuple(freqCount)].append(string) # add this string to freq map

        return list(result.values())


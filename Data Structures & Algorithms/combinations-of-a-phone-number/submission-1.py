class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        def formSubstrings(digits:str, currIndex:int, currStr: str, result: List[str]):
            if currIndex == len(digits):
                result.append(currStr)
                return

            letters = digitToChars[digits[currIndex]]
            for c in letters:
                currStr = currStr + c
                formSubstrings(digits, currIndex + 1, currStr, result)
                currStr = currStr[:len(currStr) - 1]
            
        result = []
        if len(digits) <= 0:
            return result
        
        formSubstrings(digits, 0, "", result)

        return result

            

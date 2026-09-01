class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenMap = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for char in s:
            if char not in parenMap.keys() and char not in parenMap.values():
                return False
            
            if char in parenMap.keys():
                if len(stack) == 0:
                    return False
                lastChar = stack[-1] 
                if parenMap[char] != lastChar:
                    return False
                else:
                    stack.pop()

            elif char in parenMap.values():
                stack.append(char)

        if len(stack) != 0:
            return False
            
        return True
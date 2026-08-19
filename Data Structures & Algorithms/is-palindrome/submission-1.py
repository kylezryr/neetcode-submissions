class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip string of spaces and lowercase
        string = s.replace(" ", "").lower()
        string = ''.join(char for char in string if char.isalnum())

        # double pointer
        first = 0
        last = len(string)-1

        while first < last:
            if string[first] != string[last]:
                return False
            else:
                first += 1
                last -= 1

        return True

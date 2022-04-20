# 1st Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = ""
        
        for char in s:
            if char.isalnum():
                array += char.lower()
        return array[::-1] == array
    
# 2nd Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or 
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9'))

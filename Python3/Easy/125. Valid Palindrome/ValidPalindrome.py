# 1st Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = ""
        
        for char in s:
            if char.isalnum():
                array += char.lower()
        return array[::-1] == array
    

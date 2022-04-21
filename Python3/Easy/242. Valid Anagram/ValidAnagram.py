# 1st Solution 
# Space Complexity - O(2n), iterating through 's' and 't' to find the frequency of each character that appears
# Time Complexity - O(1), sorting in place, no new arrays are created
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    
# 2nd Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for char in range(len(s)):
            countS[s[char]]= 1 + countS.get(s[char], 0)
            countT[t[char]]= 1 + countT.get(t[char], 0)
        
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        return True
            

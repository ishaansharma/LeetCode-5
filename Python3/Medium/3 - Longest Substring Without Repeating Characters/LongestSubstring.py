class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        repeated = set()
        maxL = 0
        
        for r in range(len(s)):
            while s[r] in repeated:
                repeated.remove(s[l])
                l += 1
            repeated.add(s[r])
            maxL = max(maxL, r - l + 1)
        return maxL
        

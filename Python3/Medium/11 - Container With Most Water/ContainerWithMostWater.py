# BRUTE FORCE APPROACH
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                res = max(res, area)
                
        return res


# OPTIMAL APPROACH
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            curAmt = (r - l) * min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
                res = max(curAmt, res)
            else:
                r -= 1
                res = max(curAmt, res)
        return res
            

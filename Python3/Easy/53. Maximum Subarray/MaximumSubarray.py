# Time Complexity: O(N), iterating through the length of 'nums'
# Space Complexity: o(1), since the list is not altered
# Kaden's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i 
            maxSub = max(maxSub, curSum)
        return maxSub
      

# Brute Force Approach - First Solo Attempt
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = k
        res = []

        for l in range(len(nums)):
            maxNum = float('-inf')
            for i in range(l, r):
                maxNum = max(maxNum, nums[i])
            r += 1
            res.append(maxNum)
            if r == len(nums) + 1:
                return res

        

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l, r = 0, 1
        maxD = -1
        
        while r < len(nums):
            if nums[l] < nums[r]:
                difference = nums[r] - nums[l]
                maxD = max(maxD, difference)
            else:
                l = r
            r += 1
        return maxD

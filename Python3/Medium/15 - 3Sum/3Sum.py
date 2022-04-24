class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, v in enumerate(nums):
            if v == nums[i - 1] and i > 0:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                curSum = v + nums[l] + nums[r]
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append((v, nums[l], nums[r]))
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return res
            

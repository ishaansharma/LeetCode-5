# 1st Attempt
# Time Complexity: O(n), iterating through nums
# Space Complexity: O(n), creating a new dictionary which values depends on the length of 'nums'

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        
        for i in range(len(nums)):
            dict[nums[i]] = 1 + dict.get(nums[i], 0)
            if dict[nums[i]] > 1:
                return True
        return False
            

# O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for index in range(i + 1, len(nums)):
                if target - nums[i] == nums[index]:
                    return i, index
                
# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {}
        
        for index, value in enumerate(nums):
            key = target - value
            if key in array:
                return [array[key], index]
            else:
                array[value] = index 

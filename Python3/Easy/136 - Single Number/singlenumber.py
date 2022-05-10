# First Attempt - Apr. 6
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_dict = {}
        for i in range(len(nums)):
            if nums[i] in new_dict:
                new_dict[nums[i]] += 1
            else:
                new_dict[nums[i]] = 1
        key_list = list(new_dict.keys())
        value_list = list(new_dict.values())
        position = value_list.index(1)
        return key_list[position]
            
# New 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
    

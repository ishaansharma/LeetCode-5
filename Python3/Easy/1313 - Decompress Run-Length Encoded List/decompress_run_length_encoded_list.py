class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        for i in range(0, len(nums), 2):
            for _ in range(nums[i]):
                new_list.append(nums[i+1])
        return new_list
       

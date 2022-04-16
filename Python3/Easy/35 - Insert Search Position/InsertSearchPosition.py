class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first, last = 0, len(nums) - 1

        while first <= last:
            middle = (first + last) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                first = middle + 1
            else:
                last = middle - 1
                
        middle = ((first + last) // 2) + 1
        return middle
      

# Space Complexity: O(N), iterating through the length of nums
# Time Complexity: O(1), output array doesn't count 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
      
# Thought Process
# I have to find the product of all the elements except nums[i].
#  - Use prefix and postfix
#  - Create a new list that will be returned that has the same length as the original list

# What will I be doing here?
# Shifting the list to the right for prefix and shifting the list to the left for prefix. 

#  - Iterate through the list, basically I will be shifting the list to the right when I am doing prefix. Doing this will result in a empty value in the front, 
#  I can instead set 1 in the front instead. 
#  - Postfix is same concept, but reversed. Visualizing it, I am also shifting the list 'nums' to the left, but instead of adding 1 to the beginning of the 
#  front to account for the missing value, I will have to put it in the last value. 
#  - Since I have to overwrite the previous value if I set res[i] to postfix, I can multiply them instead. After iterating through the list 'nums', I
#  can return my list 'res'.

# Time Complexity: O(log n)
# Space Complexity: 0(1)

# Original Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l + r) // 2
            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle
        return -1

# New Solution, new solution prevents overflow with other programming languages such as Java and C++ that has bounded integers (2^32). 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = l + ((r - l) // 2)
            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle
        return -1

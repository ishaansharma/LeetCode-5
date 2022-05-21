# MAX HEAP SOLUTION
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(heap)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

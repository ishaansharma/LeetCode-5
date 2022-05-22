class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        print(set(nums))
        for n in set(nums):
            if len(heap) < 3:
                heapq.heappush(heap, n)
            else:
                heapq.heappushpop(heap, n)
        if len(heap) == 3:
            return heap[0]
        else:
            return max(heap)
          

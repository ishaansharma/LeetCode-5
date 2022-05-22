class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        values = []
        
        for x, y in points:
            dist = abs(x)**2 + abs(y)**2 
            values.append([dist, x, y])
        
        res = []
        heapq.heapify(values)
        
        for i in range(k):
            dist, x, y = heapq.heappop(values)
            res.append([x, y])
        return res

# MAX HEAP
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dist = -(x**2 + y**2)
            if len(heap) == k:
                heapq.heappushpop(heap, [dist, x, y])
            else:
                heapq.heappush(heap, [dist, x, y])
        
        return [(x, y) for dist, x, y in heap]
                

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
      

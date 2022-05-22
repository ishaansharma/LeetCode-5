class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        
        time = 0
        q = deque()
        
        while heap or q:
            time += 1
            if heap:
                c = 1 + heapq.heappop(heap)
                if c:
                    q.append([c, time + n])
            if q:
                if q[0][1] == time:
                    heapq.heappush(heap, q.popleft()[0])
        return time
      

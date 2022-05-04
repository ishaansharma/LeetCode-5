class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + ((r - l) // 2)
            time = 0
            for i in piles:
                time += math.ceil(i / k)
            if time <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return res
      

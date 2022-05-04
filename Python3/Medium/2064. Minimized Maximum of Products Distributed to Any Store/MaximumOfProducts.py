class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        res = r
        
        while l <= r:
            quantity = l + ((r - l) // 2)
            amount = 0
            
            for q in quantities:
                amount += math.ceil(q / quantity)
            
            if amount <= n:
                res = min(res, quantity)
                r = quantity - 1
            else:
                l = quantity + 1
        return res
                

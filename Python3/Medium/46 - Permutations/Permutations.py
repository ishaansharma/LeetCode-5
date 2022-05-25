class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(cur):

            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if nums[i] in cur:
                    continue
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                
        dfs([])
        return res
      

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prevDay, prevTemp = stack.pop()
                res[prevDay] = day - prevDay
            stack.append([day, temp])
        return res
      

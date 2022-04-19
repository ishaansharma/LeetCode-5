class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {")": "(", "}": "{", "]": "["}
        
        for i in s:
            if i in bracket.values():
                stack.append(i)
            elif i in bracket:
                if stack == [] or bracket[i] != stack.pop():
                    return False
        return stack == []
      

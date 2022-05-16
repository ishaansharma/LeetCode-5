# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ITERATIVE BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], deque([(root, 0)])
        
        while stack:
            node, depth = stack.popleft()
            if not node:
                continue
            if len(res) == depth:
                res.append(node.val)
            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))
            
        return res 
            

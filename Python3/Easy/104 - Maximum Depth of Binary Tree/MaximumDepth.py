# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RECURSIVE DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# ITERATIVE BFS 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        stack = deque([root])
        
        while stack:
            for i in range(len(stack)):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            level += 1
        return level

# ITERATIVE DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [[root, 1]]
        
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
        return res

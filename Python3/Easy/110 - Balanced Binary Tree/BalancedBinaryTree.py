# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1ST ATTEMPT BY MYSELF
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            nonlocal statement
            if not node:
                return 0   
            left = height(node.left)
            right = height(node.right)
            if left - right > 1 or right - left > 1:
                statement = False
            return 1 + max(left, right)
        statement = True
        height(root)
        return statement

# REVISED SOLUTION
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0   
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return height(root) != -1
    

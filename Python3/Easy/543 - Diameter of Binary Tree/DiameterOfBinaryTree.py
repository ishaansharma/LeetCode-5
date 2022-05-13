# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            nonlocal maxDiameter
            
            if node:
                left = depth(node.left)                                     
                right = depth(node.right)
                maxDiameter = max(maxDiameter, left + right)          # FINDS THE DIAMETER
                return 1 + max(left, right)                           # FINDS THE HEIGHT
            else:
                return 0
        maxDiameter = 0
        depth(root)
        return maxDiameter
    

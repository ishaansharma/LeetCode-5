# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxSum = root.val
        self.findSum(root)
        return self.maxSum
    
    def findSum(self, node):
        if not node:
            return 0 
        l = max(0, self.findSum(node.left))
        r = max(0, self.findSum(node.right))
        
        self.maxSum = max(self.maxSum, node.val + l + r)
        return node.val + max(l, r)
 

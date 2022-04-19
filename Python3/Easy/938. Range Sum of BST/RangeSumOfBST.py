# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ITERATIVE
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res, stack = 0, [root]

        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    res += node.val
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                if low > node.val and node.right:
                    stack.append(node.right)
                if high < node.val and node.left:
                    stack.append(node.left)
        return res
    
# RECURSION
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        self.rangeSum(root, low, high)
        return self.res
    
    def rangeSum(self, root, low, high):
        if root:
            if low <= root.val <= high:
                self.res += root.val
                if root.left:
                    self.rangeSum(root.left, low, high)
                if root.right:
                    self.rangeSum(root.right, low, high)
            elif root.val < low and root.right:
                self.rangeSum(root.right, low, high)
            elif root.val > high and root.left:
                self.rangeSum(root.left, low, high)
    

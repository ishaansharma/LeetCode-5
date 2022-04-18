# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RECURSIVE METHOD

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
        
    
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        else:
            return False

        
 # ITERATIVE METHOD

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        stack = [[root.left, root.right]]
        
        while len(stack) > 0:
            l, r = stack.pop()
            
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False
            if l.val == r.val:
                stack.append([l.left, r.right])
                stack.append([l.right, r.left])
            else:
                return False
        return True
    

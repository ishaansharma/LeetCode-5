# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# FIRST ATTEMPT, 72/80 test cases
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = deque([root])
        
        while stack:
            for i in range(len(stack)):
                node = stack.popleft()
                if not node:
                    continue
                if node.left and node.left.val >= root.val:
                    return False
                if node.right and node.right.val <= root.val:
                    return False
                stack.append(node.left)
                stack.append(node.right)
        return True

# SECOND ATTEMPT
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -float('inf'), float('inf'))]
        
        while stack:
            node, least, greatest = stack.pop()
            if node.val <= least or node.val >= greatest:
                return False
            if node.left:
                stack.append((node.left, least, node.val))
            if node.right:
                stack.append((node.right, node.val, greatest))
        return True


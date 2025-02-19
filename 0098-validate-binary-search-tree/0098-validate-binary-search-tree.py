# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBst(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return True
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if not validBst(node, lower, upper):
                return False
            if node.left:
                stack.append((node.left, lower, node.val))
            if node.right:
                stack.append((node.right, node.val, upper))
        return True


        
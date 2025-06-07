# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def isH(node):
            if not node:
                return 0
            left = isH(node.left)
            right = isH(node.right)
            if abs(left - right) > 1:
                res[0] = False
            return max(left, right) + 1
        isH(root)
        return res[0]
        
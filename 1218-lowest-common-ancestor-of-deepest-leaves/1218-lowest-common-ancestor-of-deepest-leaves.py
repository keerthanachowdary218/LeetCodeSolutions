# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def maxDepth(node):
            if not node:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))
        maxi = maxDepth(root)
        def dfs(node, maxi, length):
            if not node:
                return None
            if maxi - 1 == length:
                return node
            left = dfs(node.left, maxi, length + 1)
            right = dfs(node.right, maxi, length + 1)
            if left and right:
                return node
            return left if left else right
        return dfs(root, maxi, 0)

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        height=self.helper(root,0)
        return height
    def helper(self,node,height):
        if not node:
            return 0
        right= 1+ self.helper(node.right,height)
        left=1+self.helper(node.left,height)
        height=max(right,left)
        return height
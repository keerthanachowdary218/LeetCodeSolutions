# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.helper(root) 
    def isLeaf(self,node):
            if not node.left and not node.right:
                return True
            return False
    def helper(self,root):
            if not root:
                return float('inf')
            if self.isLeaf(root):
                return 1
            right=1+ self.helper(root.right)
            left= 1+ self.helper(root.left)
            return min(right,left)
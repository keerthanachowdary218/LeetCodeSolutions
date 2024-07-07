# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam=0
        def maxlen(node):
            if not node:
                return 0
            rightlen=maxlen(node.right)
            leftlen=maxlen(node.left)
            self.diam=max(self.diam,rightlen+leftlen)
            return 1+max(rightlen,leftlen)
        maxlen(root)
        return self.diam
        
        
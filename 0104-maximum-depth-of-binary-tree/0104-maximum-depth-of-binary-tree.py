# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        stack=([(root,0)])
        maxi=0
        while stack:
            node,hght=stack.pop()
            maxi=max(maxi,hght)
            if node.left:
                stack.append((node.left,hght+1))
            if node.right:
                stack.append((node.right,hght+1))
        return maxi+1
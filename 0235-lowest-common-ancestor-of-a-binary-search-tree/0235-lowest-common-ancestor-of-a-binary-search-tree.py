# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        prev=root
        while prev:
            if (prev.val>= p.val and prev.val<=q.val)  or (prev.val<= p.val and prev.val>=q.val):
                return prev
            elif prev.val<p.val and prev.val<q.val: 
                prev=prev.right
            else:
                prev=prev.left 
        return None
                
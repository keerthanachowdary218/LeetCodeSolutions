# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self,Node1,Node2):
        if (Node1==None and Node2!=None) or (Node2==None and Node1!=None):
            return False
        if Node1==Node2==None:
            return True
        if Node1.val==Node2.val:
            return (self.help(Node1.left,Node2.right) and self.help(Node1.right,Node2.left) )
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.help(root.left,root.right)
        return True
        
        
        
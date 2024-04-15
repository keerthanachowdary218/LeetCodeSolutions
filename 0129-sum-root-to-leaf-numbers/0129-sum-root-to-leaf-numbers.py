# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack=[(root,0)]
        total_sum=0
        while stack:
            node,res=stack.pop()
            res=node.val+res*10
            if not node.left and not node.right:
                total_sum += res
            else:
                if node.left:
                    stack.append([node.left,res])
                if node.right:
                    stack.append([node.right,res])
        return (total_sum)
        
        
        
        

        
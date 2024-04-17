# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return None
        stack=[[root,chr(root.val + ord('a'))]]
        lexi=[]
        while stack:
            node,curstr=stack.pop()
            if not node.left and not node.right:
                lexi.append(curstr)
            if node.left:
                stack.append([node.left,chr(node.left.val + ord('a'))+curstr])
            if node.right:
                stack.append([node.right,chr(node.right.val + ord('a'))+curstr])
        return min(lexi)
                
 
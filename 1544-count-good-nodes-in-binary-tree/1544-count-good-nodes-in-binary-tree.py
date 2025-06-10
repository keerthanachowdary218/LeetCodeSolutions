# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=[0]
        def dfs(node,maxi):
            if not node:
                return
            if maxi<=node.val:
                res[0]+=1
            maxi=max(maxi,node.val)
            dfs(node.right,maxi)
            dfs(node.left,maxi)
            return 
        dfs(root, root.val)
        return res[0]

            

        
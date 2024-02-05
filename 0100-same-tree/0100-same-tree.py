# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def Traverse(tree,treelist):
            if tree:
                treelist.append(tree.val)
                Traverse(tree.left,treelist)
                Traverse(tree.right,treelist)
            if not tree:
                treelist.append('null')
        ptree=[]
        qtree=[]
        Traverse(p,ptree)
        print(ptree)
        Traverse(q,qtree)
        print(qtree)
        if ptree==qtree:
            return True
        return False
            
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    preIdx=0
    postIdx=0
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        root=TreeNode(preorder[self.preIdx])
        self.preIdx+=1
        if root.val!=postorder[self.postIdx]:
            root.left=self.constructFromPrePost(preorder, postorder)
        if root.val!=postorder[self.postIdx]:
            root.right=self.constructFromPrePost(preorder, postorder)
        self.postIdx+=1
        return root
        
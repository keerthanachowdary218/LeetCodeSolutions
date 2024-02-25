# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #right tree balaced, left tree balanced and height diff is 1
        '''
        if not root:
            return True
        rightheight=leftheight=0
        if root.right:
            rightheight = self.isHeight(root.right)
        if root.left: 
            leftheight = self.isHeight(root.left)
        if (rightheight-leftheight)==0 or (rightheight-leftheight)==1 or (rightheight-leftheight)==-1:
            return True
        else:
            return False
    def isHeight(self,TreeNode):
        if not TreeNode:
            return 0
        else:
            return 1+max(self.isHeight(TreeNode.right),self.isHeight(TreeNode.left))
        '''
        #lets try optimising 
        return self.isHeight(root) != -1
    def isHeight(self, TreeNode):
        if not TreeNode:
            return 0
        left_height = self.isHeight(TreeNode.left)
        right_height = self.isHeight(TreeNode.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)
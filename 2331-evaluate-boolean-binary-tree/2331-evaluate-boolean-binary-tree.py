# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        stack = []
        
        def calval(node):
            if not node:
                return True  # Return True for leaf nodes
            if node.val == 2:
                left_val = calval(node.left)
                right_val = calval(node.right)
                curval = left_val or right_val
                stack.append(curval)
                print('or', stack)
            elif node.val == 3:
                left_val = calval(node.left)
                right_val = calval(node.right)
                curval = left_val and right_val
                stack.append(curval)
                print('and', stack)
            else:
                curval = node.val
            return curval
        
        val = calval(root)
        return val
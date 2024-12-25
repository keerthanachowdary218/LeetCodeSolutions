# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None:
            return result
        process = [(root, 1)]
        while len(process) > 0:
            node, level = process.pop()
            if len(result) < level:
                result.append(node.val)
            else:
                result[level - 1] = max(result[level - 1], node.val)
            if node.left != None:
                process.append((node.left, level + 1))
            if node.right != None:
                process.append((node.right, level + 1))   
        return result
        
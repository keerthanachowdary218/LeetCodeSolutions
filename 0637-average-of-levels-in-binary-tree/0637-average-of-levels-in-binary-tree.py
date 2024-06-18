# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = [(root, 0)]
        res = []
        while queue:
            node, level = queue.pop(0)
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        print(res)
        avgg=[]
        for i in res:
            summ=0
            for j in i:
                summ+=j
            avg=summ/len(i)
            avgg.append(avg)
        return avgg
            
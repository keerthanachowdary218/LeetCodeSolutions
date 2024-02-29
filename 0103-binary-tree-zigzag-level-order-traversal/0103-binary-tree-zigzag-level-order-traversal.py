# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        que=deque()
        if not root:
            return []
        que.append((root,0))
        while que:
            node,lenn=que.popleft()
            if len(res) <= lenn:
                res.append([])
            res[lenn].append(node.val)
            
            if node.left:
                    que.append((node.left,1+lenn))
            if node.right:
                    que.append((node.right,1+lenn))
        for i in range(len(res)):
            if i%2==1:
                res[i]=res[i][::-1]  
        return (res)
                
            
        
        
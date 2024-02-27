# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        que=deque()
        if not root: 
            return []
        que.append((root,0))
        height=0
        while que:
            node,lenn=que.popleft()
            print(len(res),lenn)
            if len(res) <= lenn:
                res.append([])
            print(node.val)
            res[lenn].append(node.val)
            height=lenn+1
            if node.left:
                #leftlen+=1
                que.append((node.left,height))
            if node.right:
                #rightlen+=1
                que.append((node.right,height))
            
        return (res)
        
        
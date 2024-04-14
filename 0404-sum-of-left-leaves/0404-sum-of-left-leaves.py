# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que=[]
        que.append([root,0])
        res=0
        while que:
            currnode,flag=que.pop()
            if flag==1:
                res+=currnode.val
            if currnode.left:
                if not currnode.left.left and not currnode.left.right: 
                    que.append([currnode.left,1])
                else:
                    que.append([currnode.left,0])
            if currnode.right:
                que.append([currnode.right,0])
        return (res)
            
                
        
        
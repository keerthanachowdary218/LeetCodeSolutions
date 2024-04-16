# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return None
        que=deque()
        que.append([root,1])
        if depth==1:
            newroot=TreeNode(val)
            newroot.left=root
            return newroot
        while que:
            node,curdepth=que.popleft()
            if curdepth==depth-1:
                newrightnode=TreeNode(val)
                newleftnode=TreeNode(val)
                newleftnode.left=node.left
                newrightnode.right=node.right
                node.left=newleftnode
                node.right=newrightnode
            if curdepth>=depth:
                return root
            if node.left:
                que.append([node.left,curdepth+1])
            if node.right:
                que.append([node.right,curdepth+1])
        
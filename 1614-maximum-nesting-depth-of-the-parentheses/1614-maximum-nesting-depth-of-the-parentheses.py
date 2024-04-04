class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        maxi=0
        for i in s:
            if i=='(':
                stack.append(i)
            if i==')':
                stack.pop(-1)
            maxi=max(len(stack),maxi)
        print(maxi)
        return maxi
                    
            
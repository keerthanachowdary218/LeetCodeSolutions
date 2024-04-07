class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        index=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            if s[i]==')':
                if len(stack)==0:
                    index.append(i)
                elif stack[-1]=='(':
                    stack.pop()
        res=''
        print(index)
        for i in range(len(s)):
            if i not in index:
                res += s[i]
        print(res)
        if len(stack)>0:
            s=''
            for i in range(len(res)-1,-1,-1):
                if res[i]=='(' and len(stack)!=0:
                    stack.pop()
                else:
                    s += res[i]  
            res=s[::-1]
            print("inside res",res)
        return res
                
        
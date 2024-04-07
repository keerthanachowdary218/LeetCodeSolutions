class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        index=[]
        #testing if open and closed brackets are correct , if not i am storing the index values of closed brackets and automatically we will be storing the open brackets in stack.
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            if s[i]==')':
                if len(stack)==0:
                    index.append(i)
                elif stack[-1]=='(':
                    stack.pop()
        res=''
        #removing the index values(clodes brackets)
        for i in range(len(s)):
            if i not in index:
                res += s[i]
        #checking if there are any redundant open brackets and removing them.
        if len(stack)>0:
            s=''
            for i in range(len(res)-1,-1,-1):
                if res[i]=='(' and len(stack)!=0:
                    stack.pop()
                else:
                    s += res[i]  
            #since we are traversing and adding in reverse order we are reversngt he string at the end
            res=s[::-1]
        return res
                
        
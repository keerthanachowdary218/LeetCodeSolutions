class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        '''
        while s:
            if part in s:
                s=s.replace(part,'')
            else:
                return s
        '''
        stack=[]
        n=len(part)
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack)>=n:
                if "".join(stack[-n:]) == part:
                    for _ in range(n):
                        stack.pop()
        return "".join(stack)


        return(s)
                
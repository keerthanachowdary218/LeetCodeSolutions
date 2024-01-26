class Solution:
    def isValid(self, s: str) -> bool:
        def checkStackEmpty(stacky) ->bool:
            if not stacky:
                return True
            return False
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif stack :
                if i == ')' and stack[-1]=='(':
                    stack.pop()
                elif i == ']' and stack[-1]=='[':
                    stack.pop()
                elif i == '}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        return checkStackEmpty(stack)
            
        
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack=[]
        for i in s:
            if i.isalpha():
                stack.append(i)
        for i in range(0,len(s)):
            if s[i].isalpha():
                s = s[:i] + stack.pop() + s[i+1:]
        return s
        
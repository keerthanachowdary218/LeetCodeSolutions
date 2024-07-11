class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(letter,num):
            return chr(ord(letter)+num)
        res=''
        for i in range(0,len(s)):
            if i%2!=0:
                k=shift(s[i-1],int(s[i]))
                res+=k
            else:
                res+=s[i]
        return res
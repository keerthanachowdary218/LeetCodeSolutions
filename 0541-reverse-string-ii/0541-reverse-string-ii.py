class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        count=0
        s = list(s)
        while i<len(s):
            if count%2==0:
                s[i:i+k]=s[i:i+k][::-1]
            else:
                s[i:i+k]=s[i:i+k]
            i=i+k
            count+=1
        res=''.join(s)
        return res
        
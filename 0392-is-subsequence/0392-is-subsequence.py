class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        if len(t)>0:
            if s[0]==t[0]:
                return self.isSubsequence(s[1:len(s)+1],t[1:len(t)+1])
            else:
                return self.isSubsequence(s,t[1:len(t)+1])
        else:
            return False
        
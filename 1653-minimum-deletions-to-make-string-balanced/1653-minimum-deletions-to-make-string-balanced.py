class Solution:
    def minimumDeletions(self, s: str) -> int:
        countb=0
        res=0
        for i in s:
            if i=='b':
                countb+=1
            elif countb:
                res+=1
                countb-=1
        return res
        
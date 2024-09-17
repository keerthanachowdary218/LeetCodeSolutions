class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1+' '+s2
        s=s.split()
        hashh=dict()
        for i in s:
            if i in hashh:
                hashh[i]+=1
            else:
                hashh[i]=1   
        res=[]
        for i in hashh:
            if hashh[i]==1:
                res.append(i) 
        return res
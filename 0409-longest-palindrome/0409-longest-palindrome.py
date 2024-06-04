class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapp={}
        for i in s:
            if i in mapp:
                mapp[i]+=1
            else:
                mapp[i]=1
        res=0 
        oddflag=0
        for i in mapp:
            if mapp[i]%2==0:
                res+=mapp[i]
            else:
                oddflag=1
                res+=(mapp[i]-1)
        return (res+oddflag)
    
        
        
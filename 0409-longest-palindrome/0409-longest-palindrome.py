class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapp={}
        for i in s:
            if i in mapp:
                mapp[i]+=1
            else:
                mapp[i]=1
        print(mapp)
        res=0 
        flag=0
        for i in mapp:
            if mapp[i]%2==0:
                res+=mapp[i]
            else:
                flag=1
                res+=(mapp[i]-1)
        return (res+flag)
    
        
        
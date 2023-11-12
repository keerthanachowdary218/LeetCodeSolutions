class Solution:
    def myPow(self, x: float, n: int) -> float:
        print(float(pow(x,n)))
        ans=1.0
        k=n
        print(n)
        if(n<0):
            n=(-1)*n
        
        while(n>0):
            if n%2==0:
                x=x*x
                n=n/2
            elif n%2!=0:
                ans=ans*x
                n=n-1
        if(k<0):
            ans=(1/ans)
        return ans
        
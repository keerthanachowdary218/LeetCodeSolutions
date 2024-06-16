class Solution:
    def sumZero(self, n: int) -> List[int]:
        res=[]
        if n%2==0:
            k=n//2
            for i in range(1,k+1):
                res.append(i)
                res.append(-i)
        else:
            k=(n-1)//2
            for i in range(1,k+1):
                res.append(i)
                res.append(-i)
            res.append(0)
        return res
        
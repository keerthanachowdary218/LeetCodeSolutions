class Solution:
    def isUgly(self, n: int) -> bool:
        if n>0:
            for p in [2,3,5]:
                while n%p==0:
                    n=n//p
        if n==1:
            return True
        else:
            False
        
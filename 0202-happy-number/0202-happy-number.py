class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n not in seen and n!=1:
            seen.add(n)
            n=sum(int(i)**2 for i in str(n))
        if n==1:
            return True
        else :
            False
        
        
class Solution:
    def numSteps(self, s: str) -> int:
        num=int(s,2)
        count=0
        while num!=1:
            count+=1
            if num%2!=0:
                num+=1
            else:
                num=num//2
        return count
        
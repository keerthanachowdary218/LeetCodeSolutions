class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness=sorted(happiness)[::-1]
        #3,2,1
        res=0
        count=0
        while k>0:
            res+=max(happiness[count]-count,0)
            count+=1
            k-=1
        return res
        
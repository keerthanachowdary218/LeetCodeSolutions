class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res=0
        for i in range(0,len(tickets)):
            #if i pointer is less than k 
            if i<=k:
                if tickets[k]<=tickets[i]:
                    res+=tickets[k]
                else:
                    res+=tickets[i]
            #if i is after k that mean one point should be decreased from k and follow above steps.
            else:
                res+=min(tickets[k]-1,tickets[i])
            print(res)
        return (res)
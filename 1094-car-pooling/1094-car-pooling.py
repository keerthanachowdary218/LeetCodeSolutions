class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start=0
        end=float('-inf')
        curcap=0
        ans=[]
        for i in range(len(trips)):
                end=max(trips[i][2],end)
        while start<end:
            curcap=0
            for i in range(len(trips)):
                if trips[i][1]<=start and trips[i][2]>=start+1:
                    curcap+=trips[i][0]
            if curcap>capacity:
                return False
            start+=1
        print(ans)
        return True
    #below code takes o(n) but space complexity is there too
        '''
        pas = [0]*1001
        for a, s, e in trips:
            pas[s] += a
            pas[e] -= a
        res = 0
        for n in pas:
            res += n
            if res > capacity:
                return False
        return True
        '''
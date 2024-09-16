class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res=[]
        for i in timePoints:
            k=i.split(':')
            res.append(int(k[0])*60+int(k[1]))
        #print(res)
        res.sort()
        ans = min(res[i + 1] - res[i] for i in range(len(res) - 1))
        return min(ans, 24 * 60 - res[-1] + res[0])
        
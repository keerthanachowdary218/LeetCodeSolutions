class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        totalObserv=n+len(rolls)
        sumObserv=mean*totalObserv
        remain=sumObserv-sum(rolls)
        if remain > n * 6 or remain < n:
            return []
        res = [1] * n
        remain -= n
        i = 0
        while remain > 0:
            res[i] += min(5,remain)
            remain -= 5
            i += 1
            '''
            add = min(5,remain)
            res[i] += add
            remain -= add
            i += 1'''
        return res
        
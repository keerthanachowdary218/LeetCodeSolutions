class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and trust==[]:
            return 1
        Arr=[0]*(n+1)
        for listt in trust:
            Arr[listt[0]]-=1
            Arr[listt[1]]+=1
        for i,val in enumerate(Arr):
            if val==n-1:
                return i
            else:
                ans=-1
        return ans
        print(Arr)
        
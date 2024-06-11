class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mapp={}
        for i in arr2:
            mapp[i]=0
        rest=[]
        for i in arr1:
            if i in mapp:
                mapp[i]+=1
            else:
                rest.append(i)
        res=[]
        for i in mapp:
            for j in range(0,mapp[i]):
                res.append(i)
        res.extend(sorted(rest))
        return res
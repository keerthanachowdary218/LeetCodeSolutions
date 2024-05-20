class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mapp={}
        for i in nums:
            if i not in mapp:
                mapp[i]=1
            else:
                mapp[i]+=1
        mapp=dict(sorted(mapp.items(), key = lambda x: (x[1], -x[0])))
        res=[]
        for i in mapp:
            for j in range(mapp[i]):
                res.append(i)
        return res
        
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mapp={}
        for i in nums:
            if i in mapp:
                mapp[i]+=1
            else:
                mapp[i]=1
        for i in mapp:
            if mapp[i]==1:
                ans=i
        return ans
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if ((len(nums)%3)!=0):
            return []
        nums.sort()
        res=[]
        i=0
        while i<len(nums):
            if(nums[i+2]-nums[i]<=k):
                res.append(nums[i:i+3])
            else:
                return [] 
            i=i+3
        return res
            
        
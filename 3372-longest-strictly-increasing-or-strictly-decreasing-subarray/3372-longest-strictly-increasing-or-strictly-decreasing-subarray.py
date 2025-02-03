class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        strictInc=0
        count=1
        for i in range(0,len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
            else:
                strictInc=max(strictInc,count)
                count=1
        strictInc=max(strictInc,count)
        print(strictInc)
        strictDec=0
        count=1
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
            else:
                strictDec=max(strictDec,count)
                count=1
        strictDec=max(strictDec,count)
        return max(strictDec,strictInc)
        
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cursum=nums[0]
        summ=cursum
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                cursum+=nums[i]
            else:
                summ=max(summ,cursum)
                cursum=nums[i]
        summ=max(summ,cursum)
        return summ

        
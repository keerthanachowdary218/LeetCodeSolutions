class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        summ=0
        for i in nums:
            summ=summ+i
        actualsumm=(n*(n+1))/2
        missing=actualsumm-summ
        return int(missing)
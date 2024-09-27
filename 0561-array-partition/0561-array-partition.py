class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        print(nums)
        i,summ=0,0
        while i<len(nums):
            summ+=nums[i]
            i+=2
        return summ
        
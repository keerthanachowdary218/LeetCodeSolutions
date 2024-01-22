class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)>=1:
            i=0
            j=i+1
            while i<j and j<len(nums):
                if nums[i]==0:
                    if nums[j]!=0:
                        nums[i],nums[j]=nums[j],nums[i]
                        i=i+1
                    if nums[j]==0:
                        j=j+1
                else:
                    i=i+1
                    j=j+1
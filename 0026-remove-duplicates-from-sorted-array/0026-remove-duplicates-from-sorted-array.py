class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #inplace
        j=1
        i=0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                i=i+1
                continue
            else:
                nums[j]=nums[i+1]
                j=j+1
                i=i+1
                continue
        return j
        
        
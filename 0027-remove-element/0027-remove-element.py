class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==1:
            if val==nums[0]:
                return 0
            return 1
        if len(nums)>1:
            i=0
            j=len(nums)-1
            while i<=j and j>=1:
                if nums[i]==val and nums[j]!=val:
                    nums[i],nums[j]=nums[j],nums[i]
                    i=i+1
                    j=j-1
                if nums[i]!=val:
                    i=i+1
                elif nums[j]==val:
                    j=j-1
            return (len(nums[0:i]))
        return 0
        
            
        
        
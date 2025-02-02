class Solution:
    def check(self, nums: List[int]) -> bool:
        '''
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                break
        if nums[-1]<nums[i] or i+1==len(nums)-1:
            return True
        else:
            return False
        '''
        count=0
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%(len(nums))]:
                count+=1
                if count>1:
                    return False
        return True
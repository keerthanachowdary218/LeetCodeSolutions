class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi=-float('inf')
        for i in range(0,len(nums)):
            if maxi<nums[i]:
                maxi=nums[i]
                maxiindex=i
        for i in range(0,len(nums)):
            if i!=maxiindex and maxi<2*nums[i]:
                return -1
        return maxiindex
                
            
        
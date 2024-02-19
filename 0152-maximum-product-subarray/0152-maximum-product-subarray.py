class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        mini=maxi=1
        for i in range(len(nums)):
            k=nums[i],nums[i]*mini,nums[i]*maxi
            maxi=max(k)
            mini=min(k) 
            print(maxi,mini)
            res=max(res,maxi)
        return res
                
            
        
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left,right=0,0
        maxi=-1
        for i in nums:
            maxi=max(maxi,i)
        print(maxi)
        count_maxi=0
        res=0
        
        while right<len(nums) and left<len(nums):
            if nums[right] == maxi:
                count_maxi+=1
            if count_maxi>=k:
                #print(res,nums[left:right+1])
                res=res+1
                if right!=len(nums):
                    res+=len(nums)-right-1
                    #print(res)
                if nums[left] == maxi:
                        count_maxi-=1
                left=left+1
                count_maxi-=1
                right=right-1
            right=right+1
        #print(res)
        return res
                
               
                
                
                
                
            
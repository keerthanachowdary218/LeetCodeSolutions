class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        max=float(-inf)
        sum=0
        for i in range(0,n):
            sum=sum+nums[i]
            if(max<sum):
                max=sum
                #print(max)
            if(sum<0):
                sum=0
        if(max<=0):
            for i in range(0,n):
                if(max<nums[i]):
                    max=nums[i]
        return max
    
 

                
                
            
        
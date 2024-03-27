class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #below is navie solution - time limit exceeds.
        '''
        def prod(n):
            if len(n)>0:
                res=n[0]
                for i in range(1,len(n)):
                    res=res*n[i]
            else:
                res=0   
            return res
        count=0
        for i in nums:
            if i>=k:
                count+=1
        if count==len(nums):
            return 0
        else:
            count=0
            #ans=[]
            for i in range(0,len(nums)):
                for j in range(i,len(nums)):
                    if prod(nums[i:j+1])<k:
                        #ans.append(nums[i:j+1])
                        count=count+1 
            return count
         '''
        if k <= 1:
            return 0
        left, right, product, count = 0, 0, 1, 0
        n = len(nums)
        while right < n:
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += 1 + (right - left)
            right += 1
        return count
        
        
        
        
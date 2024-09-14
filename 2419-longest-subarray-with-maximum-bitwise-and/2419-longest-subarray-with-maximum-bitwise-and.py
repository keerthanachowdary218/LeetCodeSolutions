class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #and -- if small num is and with large number the total and is small.. so longest subarray shld be of max number
        maxi=max(nums)
        lenn=1
        count=0
        for i in nums:
            if i==maxi:
                count+=1
                lenn=max(lenn,count)
            else:
                count=0
        return lenn
        '''
        maxi=max(nums)
        maxar=1
        for i in range(0,len(nums)):
            andv=nums[i]
            for j in range(i+1,len(nums)):
                andv=nums[j]&andv
                if maxi<=andv:
                    maxar=max(maxar,j-i+1)
                    maxi=max(maxi,andv)
        return maxar
        '''
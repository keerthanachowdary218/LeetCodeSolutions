class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        curbit = 0
        maxlen = 0
        while r < len(nums):
            while curbit & nums[r] != 0:
                curbit ^= nums[l] 
                l += 1  
            print(l,r,curbit)
            curbit |= nums[r] 
            print(l,r,curbit)
            maxlen = max(maxlen, r - l + 1)  
            r += 1  
        return maxlen
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        print(nums)
        maxlen=curlen=i=0
        j=1
        if(len(nums)==0):
            return 0
        while i<j and i<len(nums) and j<len(nums):
            if nums[j]==nums[i]+curlen+1:
                print(i,j)
                j=j+1
                curlen=curlen+1
                print(curlen,maxlen)
                if curlen>maxlen:
                    maxlen=curlen
                continue
            print(curlen)
            print(maxlen)
            i=j
            j=i+1
            curlen=0
        return maxlen+1
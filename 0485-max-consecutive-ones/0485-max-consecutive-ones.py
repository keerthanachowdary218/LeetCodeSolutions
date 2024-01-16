class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currcount=0
        maxcount=0
        for i in nums:
            if i==1:
                currcount=currcount+1
            else:
                currcount=0
            if maxcount<currcount:
                maxcount=currcount
        return maxcount
        
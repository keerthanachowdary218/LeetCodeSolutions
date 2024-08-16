class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=0
        for i in nums:
            rightsum+=i
        #print(leftsum,rightsum)
        for i in range(0,len(nums)):
            rightsum-=nums[i]
            #print(leftsum,rightsum)
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1
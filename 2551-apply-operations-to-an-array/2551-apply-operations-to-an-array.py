class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        result = []
        zc = 0
        for i in nums:
            if i!=0:
                result.append(i)
            else:
                zc += 1
        result.extend([0]*zc)
        return result
        
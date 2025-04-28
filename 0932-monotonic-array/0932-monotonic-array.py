class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def mono(nums):
            count=1
            for i in range(1,len(nums)):
                if nums[i-1]<=nums[i]:
                    count+=1
            if count!=len(nums):
                return False
            else:
                return True
        return mono(nums) or mono(nums[::-1])
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        Time limit exceeded 
        res=[]
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
        return res
        '''
        numSet = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in numSet]



        
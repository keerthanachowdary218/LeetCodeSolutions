class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for l, r in queries:
            prefix[l] -= 1
            prefix[r + 1] += 1
        d = 0
        for i in range(n):
            d += prefix[i]
            if nums[i] + d > 0:
                return False
        return True
        '''
        for query in queries:
            for i in range(query[0],query[1]+1):
                if nums[i]==0:
                    continue
                else:
                    nums[i]-=1
        for i in nums:
            if i!=0:
                return False
        return True
        '''

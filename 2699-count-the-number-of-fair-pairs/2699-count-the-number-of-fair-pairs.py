class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        '''
        #brute force
        res=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                summ=nums[i]+nums[j]
                if i<j and summ<=upper and lower<=summ:
                    res+=1
        return res
        '''
        def binary_search_left(nums, low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        def binary_search_right(nums, low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n):
            left = binary_search_left(nums, i + 1, n - 1, lower - nums[i])
            right = binary_search_right(nums, i + 1, n - 1, upper - nums[i])
            res += (right - left + 1) if right >= left else 0
        return res
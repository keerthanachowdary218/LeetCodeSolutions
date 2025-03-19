class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt = 0

        for i in range(n):
            if nums[i] == 0 and i + 2 < n:
                nums[i] = 1
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                cnt += 1

        for i in range(n):
            if nums[i] == 0:
                return -1

        return cnt
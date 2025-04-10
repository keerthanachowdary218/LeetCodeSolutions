class Solution(object):
    def canPartition(self,nums):
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        n = len(nums)
        dp = [[None] * (n + 1) for _ in range(target + 1)]
        for j in range(n + 1):
            dp[0][j] = True
        def helper(remaining_sum, index):
            if dp[remaining_sum][index] is not None:
                return dp[remaining_sum][index]
            if index >= n:
                return False
            take = False
            if nums[index] <= remaining_sum:
                take = helper(remaining_sum - nums[index], index + 1)
            skip = helper(remaining_sum, index + 1)
            dp[remaining_sum][index] = take or skip
            return dp[remaining_sum][index]
        return helper(target, 0)
        
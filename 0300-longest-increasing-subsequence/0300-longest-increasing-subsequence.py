class Solution:
    def f(self, nums, ind, prev_index, dp):
        if ind == len(nums):
            return 0
        if dp[prev_index][ind] != -1:
            return dp[prev_index][ind]
        # Calculate length if the current element is not taken
        nottake = self.f(nums, ind + 1, prev_index, dp)
        # Calculate length if the current element is taken
        takelen = 0
        if prev_index == -1 or nums[ind] > nums[prev_index]:
            takelen = 1 + self.f(nums, ind + 1, ind, dp)
        # Store the result in dp array
        dp[prev_index][ind] = max(nottake, takelen)
        return dp[prev_index][ind]
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums))]
        res = self.f(nums, 0, -1, dp)
        return res
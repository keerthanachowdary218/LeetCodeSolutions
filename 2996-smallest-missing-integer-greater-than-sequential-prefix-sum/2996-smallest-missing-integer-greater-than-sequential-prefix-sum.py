class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum_val = 0
        ind = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i + 1] == nums[i] + 1:
                sum_val += nums[i]
                ind = i
            else:
                ind = i
                break
        if ind == n - 2 and nums[n - 2] + 1 == nums[n - 1]:
            sum_val += nums[n - 1]
        else:
            sum_val += nums[ind]
        while sum_val in nums:
            sum_val += 1
        return sum_val
        
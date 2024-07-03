class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        print(nums)
        ans = nums[-1] - nums[0]
        #greedy approach
        #you can change either 3 maximums, or 2 maximums and one minimum and so on.
        for i in range(4):
            print(nums[-(4 - i)] - nums[i])
            ans = min(ans, nums[-(4 - i)] - nums[i])
        return ans
        
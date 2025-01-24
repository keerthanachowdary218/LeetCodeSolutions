class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        a=0
        n=len(nums)
        for i in range(n-1):
            a=max(a,abs(nums[i]-nums[i+1]))
        a = max(a, abs(nums[n - 1] - nums[0]))
        return a
        
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
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
        
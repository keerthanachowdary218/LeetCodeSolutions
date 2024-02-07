class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        subarrays = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if len(nums[i:j+1]) >= 1:
                    subarrays.append(set(nums[i:j+1]))
        res = 0
        for value in subarrays:
            res += len(value) * len(value)
        return res
        
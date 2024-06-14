class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        numTracker = 0
        minIncreament = 0
        #unique elements not the continuous elements.
        for num in nums:
            numTracker = max(numTracker, num)
            minIncreament += numTracker - num
            numTracker += 1
        return minIncreament
        
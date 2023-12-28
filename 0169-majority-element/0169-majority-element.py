import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        left = self.majorityElement(nums[:mid])
        right= self.majorityElement(nums[mid:])
        if left == right:
            return left
        left_count = nums.count(left)
        right_count = nums.count(right)
        return left if left_count > right_count else right

            
        
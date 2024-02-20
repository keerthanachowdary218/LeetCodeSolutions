class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)

        mid = (len(nums) - 1) // 2
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[mid] < nums[r]:
            return nums[l]
        elif nums[mid] > nums[r]:
            return self.findMin(nums[mid+1:])
        elif nums[l] > nums[mid]:
            return self.findMin(nums[l:mid+1])

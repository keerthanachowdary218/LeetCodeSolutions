class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)-1):
            if nums[i]%2== nums[i+1]%2:
                return False
        return True

        
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        countt=0
        for i in range(0,len(nums)):
            if bin(i).count('1')==k:
                print(i)
                countt+=nums[i]
        return countt
        
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        left,right=0,0
        maxi=-1
        Hmap={}
        while right <len(nums) and left <len(nums):
            if nums[right] in Hmap:
                Hmap[nums[right]]+=1
            else:
                Hmap[nums[right]]=1
            while Hmap[nums[right]]>k:
                Hmap[nums[left]]-=1
                if Hmap[nums[left]] == 0:
                    del Hmap[nums[left]]
                left=left+1
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi
    
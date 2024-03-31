'''class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left,right,goodsubarrays=0,0,0
        unique={}
        while left<=right and right<len(nums):
            if len(unique)<=k:
                if nums[right] not in unique:
                    unique[nums[right]]=1
                else:
                    unique[nums[right]]+=1
            if len(unique)==k:
                print(nums[left:right+1])
                goodsubarrays=goodsubarrays+1
                subright=right+1
                while subright<len(nums):
                    if nums[subright] in unique:
                        print(nums[left:subright+1])
                        goodsubarrays=goodsubarrays+1
                    else:
                        break
                    subright=subright+1
                unique[nums[left]]-=1
                if (unique[nums[left]]==0):
                    del unique[nums[left]]
                left+=1
                # Move right pointer forward to maintain exactly k distinct elements
                right = left  
                
                # Adjust right pointer if it exceeds array bounds
                if right >= len(nums):
                    break
            right=right+1
        return (goodsubarrays)
'''
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(nums, k):
            niceSubarray = 0
            hashmap = {}
            left, right = 0, 0
            while right < len(nums):
                if nums[right] in hashmap:
                    hashmap[nums[right]] += 1
                else:
                    hashmap[nums[right]] = 1
                while len(hashmap) > k:
                    hashmap[nums[left]] -= 1
                    if hashmap[nums[left]] == 0:
                        del hashmap[nums[left]]
                    left += 1
                niceSubarray += right - left + 1
                right += 1
            return niceSubarray
        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)
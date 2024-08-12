class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        smallnums1=nums1[0]
        smallnums2=nums2[0]
        for i in nums1:
            if i<smallnums1:
                smallnums1=i
        for i in nums2:
            if i<smallnums2:
                smallnums2=i
        #print(smallnums1,smallnums2)
        return smallnums2-smallnums1
        
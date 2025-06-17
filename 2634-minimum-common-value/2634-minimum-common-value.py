class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1]<nums2[0]:
            return -1
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                return nums1[i]
        return -1
        
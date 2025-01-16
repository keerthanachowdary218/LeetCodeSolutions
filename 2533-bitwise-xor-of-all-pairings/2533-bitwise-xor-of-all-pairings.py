class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        res=[]
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                res.append(nums1[i]^nums2[j])
        print(res)
        ans=0
        for i in res:
            ans=ans^i
        return ans
        '''
        len1, len2 = len(nums1), len(nums2)
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num, 0) + len2
        for num in nums2:
            freq[num] = freq.get(num, 0) + len1
        ans = 0
        for num in freq:
            if freq[num] % 2:
                ans ^= num
        return ans


        
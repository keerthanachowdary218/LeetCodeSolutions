class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(0,len(nums2)):
            flag=0
            for j in range(i+1,len(nums2)):
                if nums2[i]<nums2[j]:
                    flag=1
                    res.append(nums2[j])
                    break
            if flag==0:
                res.append(-1)
        ans=[]
        for i in nums1:
            for j in range(0,len(nums2)):
                if i==nums2[j]:
                    ans.append(res[j])
                    break
        #print(res,ans)
        return ans
        
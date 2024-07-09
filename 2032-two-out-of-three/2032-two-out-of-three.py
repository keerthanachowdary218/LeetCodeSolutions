class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result=nums1+nums2+nums3
        #print(result)
        setnums=set(result)
        hashh={}
        for i in setnums:
            hashh[i]=0
        for i in setnums:
            if i in nums1:
                hashh[i]+=1
            if i in nums2:
                hashh[i]+=1
            if i in nums3:
                hashh[i]+=1
        #print(hashh)
        res=[]
        for i in hashh:
            if hashh[i]>=2:
                res.append(i)
        return res
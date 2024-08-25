class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in range(0,len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort()
        odd=odd[::-1]
        res=[]
        i=0
        while i<len(nums):
            if i%2==0:
                #print(i//2)
                res.append(even[i//2])
            else: 
                #print(i//2)
                res.append(odd[i//2])
            i+=1
        return res
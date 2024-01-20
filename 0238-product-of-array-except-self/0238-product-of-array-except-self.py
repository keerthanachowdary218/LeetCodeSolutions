class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        if 0 not in nums:
            result=[]
            for i in nums:
                    mul=mul*i
            for i in nums:
                result.append((mul//i))
            return result
        else:
            result=[]
            countZeroes=0
            for i in nums:
                if i!=0:
                    mul=mul*i
                else:
                    countZeroes=countZeroes+1
            if countZeroes>1:
                mul=0
            for i in nums:
                if i==0:
                    result.append(mul)
                else:
                    result.append(0)
            return result
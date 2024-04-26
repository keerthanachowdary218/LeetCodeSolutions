class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashh={}
        for i in nums:
            if i not in hashh:
                hashh[i]=1
            else:
                hashh[i]+=1
        sorted_hashh = dict(sorted(hashh.items()))
        #new_hashh - to keep track of count of less then i
        new_hashh={}
        count=0
        for i in sorted_hashh:
            new_hashh[i]=count
            count+=sorted_hashh[i]
        res=[]
        for i in nums:
            res.append(new_hashh[i])
        return res
            
                    
                    
                
            
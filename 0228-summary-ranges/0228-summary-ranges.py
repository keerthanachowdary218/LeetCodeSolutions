class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums==[]:
            return []
        count=nums[0]
        i=0
        res=[[]]
        k=0
        while i<len(nums):
            if nums[i]==count:
                print(count)
                res[k].append(nums[i])
                count+=1
                i+=1
            else:
                print(i)
                count=nums[i]
                res.append([])
                k+=1
        #print(res)
        ans=[]
        for r in res:
            if len(r)>1:
                ans.append(f"{r[0]}->{r[-1]}")
                
            else:
                ans.append(str(r[0]))
        return ans
            
        
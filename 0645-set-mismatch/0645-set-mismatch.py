class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        summ=sum(nums)
        n=len(nums)
        actual=(n*(n+1))/2
        print(summ,actual)
        setnum=set()
        for i in nums:
            if i in setnum:
                repnum=i
            else:
                setnum.add(i)
        actualnum = int(repnum+actual-summ)
        return [repnum,actualnum]
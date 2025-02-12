class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashh=defaultdict(list)
        for num in nums:
            summ=0
            for digit in str(num):  
                summ += int(digit)       
            hashh[summ].append(num)
        print(hashh)
        for i in hashh:
            hashh[i]=sorted(hashh[i])
        print(hashh)
        maxsum=-1
        for i in hashh:
            if len(hashh[i])>=2:
                n=len(hashh[i])
                maxsum=max(maxsum,hashh[i][n-1]+hashh[i][n-2])
        return (maxsum)
        
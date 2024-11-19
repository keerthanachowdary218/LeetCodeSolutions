class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = set()
        n = len(nums)
        sum_ = 0
        mx = 0
        j = 0
        for i in range(n):
            while nums[i] in s:
                sum_ -= nums[j]
                s.remove(nums[j])
                j += 1
            
            s.add(nums[i])
            sum_ += nums[i]

            if len(s) == k:
                mx = max(mx, sum_)
                sum_ -= nums[j]
                s.remove(nums[j])
                j += 1

        return mx
        '''
        #limited exceeded
        def unique(ind):
            sett=set()
            if ind + k > len(nums):
                return False
            for i in range(ind+0,ind+k):
                if nums[i] in sett:
                    return False
                else:
                    sett.add(nums[i])
            print(sett)
            return True
        maxi=0
        for i in range(0,len(nums)-k+1):
            if unique(i):
                summ=sum(nums[i+0:i+k])
                print(summ)
                maxi=max(maxi,summ)
        return maxi
        '''
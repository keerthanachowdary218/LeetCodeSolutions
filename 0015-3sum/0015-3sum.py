class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #i+j=-k
        '''
        TLE
        pair_sums = {}
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                pair_sum = nums[i] + nums[j]
                if pair_sum not in pair_sums:
                    pair_sums[pair_sum] = [(i, j)]
                else:
                    pair_sums[pair_sum].append((i, j))
        print(pair_sums)
        for k in range(len(nums)):
            target = -nums[k]
            if target in pair_sums:
                for (i, j) in pair_sums[target]:
                    if k != i and k != j:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in res:
                            res.append(triplet)
        return res
        '''
        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)
        N, P = set(n), set(p)
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
                
                
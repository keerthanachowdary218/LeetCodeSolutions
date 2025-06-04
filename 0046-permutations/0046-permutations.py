class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(perm, used):
            if len(perm) == len(nums):
                res.append(perm[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                perm.append(nums[i])
                dfs(perm, used)
                perm.pop()
                used[i] = False
        dfs([], [False] * len(nums))
        return res
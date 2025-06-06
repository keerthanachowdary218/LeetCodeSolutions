class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for i in nums:
            new_subsets = []
            for s in subset:
                new_subsets.append(s + [i])
            subset.extend(new_subsets)
        return subset
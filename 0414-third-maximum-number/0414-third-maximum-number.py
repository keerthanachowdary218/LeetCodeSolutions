class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sett=list(set(nums))
        if len(sett)<=2:
            return max(sett)
        sortedsett=sorted(sett)
        return sortedsett[::-1][2]
        
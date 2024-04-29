class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res=0
        for i in hours:
            if i>=target:
                res+=1
        return res
        
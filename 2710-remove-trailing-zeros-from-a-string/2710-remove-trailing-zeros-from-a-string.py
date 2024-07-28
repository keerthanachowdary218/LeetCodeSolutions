class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        revnum=num[::-1]
        res=int(revnum)
        return str(res)[::-1]
        
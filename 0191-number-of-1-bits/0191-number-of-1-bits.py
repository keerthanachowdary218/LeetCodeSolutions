class Solution:
    def hammingWeight(self, n: int) -> int:
        res=bin(n).replace('0b','')
        return res.count('1')
        
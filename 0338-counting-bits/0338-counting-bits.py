class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            print(i)
            ans.append(bin(i).count('1'))
        return ans
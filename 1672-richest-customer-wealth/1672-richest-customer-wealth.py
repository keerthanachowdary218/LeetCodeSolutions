class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        row=len(accounts)
        col=len(accounts[0])
        maxi=-1
        for i in range(0,row):
            summ=0
            for j in range(0,col):
                summ+=accounts[i][j]
            maxi=max(maxi,summ)
        return maxi
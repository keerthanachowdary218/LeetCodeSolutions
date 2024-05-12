class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        res=[[0 for i in range(0,n-2)]for j in range(0,n-2)]
        for i in range(0,n-2):
            for j in range(0,n-2):
                maxi=-1
                for k in range(0,3):
                    for l in range(0,3):
                        maxi = max(maxi, grid[i+k][j+l])
                res[i][j]=maxi
        return (res)
        
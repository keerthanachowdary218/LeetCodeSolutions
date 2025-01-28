class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def isexist(i,j,r,c):
            if 0<=i<r and 0<=j<c:
                return True
            return False
        def dfs(grid,visited,i,j):
            if not isexist(i,j,r,c) or visited[i][j] or grid[i][j]==0:
                return 0
            visited[i][j]=True
            return grid[i][j]+dfs(grid,visited,i,j+1)+dfs(grid,visited,i+1,j)+dfs(grid,visited,i,j-1)+dfs(grid,visited,i-1,j)
        r,c=len(grid),len(grid[0])
        visited=[[False]*c for i in range(r)]
        res=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]!=0 and visited[i][j]==False: 
                    res=max(res,dfs(grid,visited,i,j))
        return res

        
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row = len(grid1)
        col = len(grid1[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        def dfs(grid, i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0 or visited[i][j]:
                return True
            visited[i][j] = True
            is_sub_island = grid1[i][j] == 1  # Start with assumption that it is a sub-island
            if not dfs(grid, i - 1, j):  # Up
                is_sub_island = False
            if not dfs(grid, i + 1, j):  # Down
                is_sub_island = False
            if not dfs(grid, i, j - 1):  # Left
                is_sub_island = False
            if not dfs(grid, i, j + 1):  # Right
                is_sub_island = False
            
            return is_sub_island

        res = 0
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1 and not visited[i][j]:
                    if dfs(grid2, i, j):
                        res += 1
        return res
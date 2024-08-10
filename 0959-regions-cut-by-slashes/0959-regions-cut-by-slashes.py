class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        #print(grid[0][1])
        max_color = 0
        #convert strings to grid with -1,0
        my_grid = [[0 for i in range(n*3)] for j in range(n*3)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]=="/":
                    my_grid[i*3+0][j*3+2] = -1
                    my_grid[i*3+1][j*3+1] = -1
                    my_grid[i*3+2][j*3+0] = -1
                elif grid[i][j]=="\\":
                    #print(grid[i][j],i,j)
                    my_grid[i*3+0][j*3+0] = -1
                    my_grid[i*3+1][j*3+1] = -1
                    my_grid[i*3+2][j*3+2] = -1
                    
        
        #print(my_grid)
        def dfs(x, y):
            if x < 0 or x >= n * 3 or y < 0 or y >= n * 3 or my_grid[x][y] != 0:
                return
            my_grid[x][y] = 1  # Mark the cell as visited
            # Visit all 4 possible directions (up, down, left, right)
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # Count the number of regions
        regions = 0
        for i in range(n * 3):
            for j in range(n * 3):
                if my_grid[i][j] == 0:
                    dfs(i, j)
                    regions += 1

        return regions
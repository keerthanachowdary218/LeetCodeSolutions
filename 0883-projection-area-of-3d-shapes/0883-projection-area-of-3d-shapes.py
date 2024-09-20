class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans, n = 0, len(grid)
        for i in range(n):
            maxFront = maxSide = 0
            for j in range(n):
                if grid[i][j]: ans += 1
                maxSide = max(maxSide, grid[i][j])
                maxFront = max(maxFront, grid[j][i])
            ans += maxSide + maxFront
        return ans
        
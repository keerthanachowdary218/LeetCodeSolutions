class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        ans = [[0] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                ans[j][i] = matrix[i][j]
        return ans
        
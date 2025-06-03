class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        sett=set()
        def dfs(i,j,n):
            if n==len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[n] or (i,j) in sett:
                return False
            if board[i][j]==word[n] and (i,j) not in sett:
                sett.add((i,j))
                res= dfs(i+1,j,n+1) or dfs(i,j+1,n+1) or dfs(i,j-1,n+1) or dfs(i-1,j,n+1)
                sett.remove((i,j))
                return res
            return False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
        
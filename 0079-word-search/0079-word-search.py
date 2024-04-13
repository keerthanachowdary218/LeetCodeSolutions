from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0

        def dfs(i, j, k):
            # Base case: If k reaches the length of the word, we've found a match
            if k == len(word):
                return True
            
            # Check boundaries and if the current cell matches the word character
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False

            # Mark the cell as visited (using a temporary value)
            temp = board[i][j]
            board[i][j] = '#'  # Marked as visited

            # Check adjacent cells in all four directions
            found = (dfs(i + 1, j, k + 1) or
                     dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or
                     dfs(i, j - 1, k + 1))

            # Restore the cell's original value
            board[i][j] = temp
            
            return found

        # Iterate through each cell to find the starting point of the word
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False

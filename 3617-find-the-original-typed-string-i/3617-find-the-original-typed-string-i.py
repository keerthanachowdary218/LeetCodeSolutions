class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        output = 1
        for i in range(1,n):
            if word[i] == word[i-1]:
                output += 1
        return output
        
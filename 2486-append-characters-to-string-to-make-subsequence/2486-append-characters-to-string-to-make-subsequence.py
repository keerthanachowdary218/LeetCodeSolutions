class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        else:
            i, j = 0, 0  
            while i < len(s) and j < len(t): 
                if s[i] == t[j]: 
                    j += 1
                print(j)
                i += 1  
            return len(t) - j
        
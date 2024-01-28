class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range(0,len(haystack)):
                if needle==haystack[i:len(needle)+i]:
                    return i
        return -1
        
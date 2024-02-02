class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(' ')
        while("" in s):
            s.remove("")
        return len(s[-1])
        
        
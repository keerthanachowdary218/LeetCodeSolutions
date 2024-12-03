class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=''
        ini=0
        for i in spaces:
            res+=s[ini:i]
            ini=i
            res+=' '
        res+=s[ini:len(s)]
        return res
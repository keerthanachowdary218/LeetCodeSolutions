class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res=''
        for word in words:
            res+=word[0]
        #print(res)
        if res==s:
            return True
        return False


        
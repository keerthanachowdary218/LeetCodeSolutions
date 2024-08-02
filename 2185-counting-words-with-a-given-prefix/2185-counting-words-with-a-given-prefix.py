class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res=0
        for word in words:
            count=0
            for i in range(0,len(pref)):
                if i<len(word) and word[i]==pref[i]:
                    count+=1
            if count==len(pref):
                res+=1
        return res
        
                
        
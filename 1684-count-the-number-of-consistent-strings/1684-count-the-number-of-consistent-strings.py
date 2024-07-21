class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=0
        for word in words:
            count=0
            for letter in word:
                if letter not in allowed:
                    break
                else:
                    count+=1
                if count==len(word):
                    res+=1  
        return res
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        totalword_len=(min(len(word1),len(word2)))*2
        newword=""
        for i in range(totalword_len):
            if i%2==0:
                newword+=(word1[i//2])
            else:
                
                newword+=(word2[(i//2)])
        if len(word1)>len(word2):
            newword+=(word1[(totalword_len//2):])
        elif len(word1)<len(word2):
            newword+=(word2[(totalword_len//2):])       
        return newword
            
            
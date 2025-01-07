class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for i in range(0,len(words)):
            for j in range(0,len(words)):
                if i!=j:
                    if words[i] in words[j]:
                        res.append(words[i])
                        break
        return res
            


        
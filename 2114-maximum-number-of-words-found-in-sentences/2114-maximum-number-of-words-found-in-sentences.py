class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=1
        for sentence in sentences:
            words=sentence.split(" ")
            maxi=max(maxi,len(words))
        return maxi
            
        
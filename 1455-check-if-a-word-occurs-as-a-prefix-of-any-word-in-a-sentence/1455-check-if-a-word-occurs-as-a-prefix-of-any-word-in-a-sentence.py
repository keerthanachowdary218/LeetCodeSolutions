class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split(' ')
        print(words)
        n=len(searchWord)
        for i,word in enumerate(words):
            #print(i,word[:n])
            if word[:n]==searchWord:
                return i+1
        return -1
        
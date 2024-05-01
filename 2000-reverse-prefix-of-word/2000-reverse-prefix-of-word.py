class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index=-1
        for i in range(0,len(word)):
            if word[i]==ch:
                res=word[:i+1]
                res=res[::-1]
                index=i
                break
        if index!=-1:
            for i in range(index+1,len(word)):
                res+=word[i]
            return res
        else:
            return word
                
                
        
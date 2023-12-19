class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split(" ")
        print(words)
        count=0
        for i in range((len(words)-1),-1,-1):
            if words[i]=='':
                continue
            count=count+1
            if count==1:
                result=words[i]
                continue
            result+=" "+words[i]
            print(result)
        return result
           
        
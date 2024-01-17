class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelslist=[]
        indexlist=[]
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        for i in range(0,len(s)):
            if s[i] in vowels:
                vowelslist.append(s[i])
                indexlist.append(i)
        vowelslist.reverse()
        s=list(s)
        count=0
        for i in indexlist:
            s[i]=vowelslist[count]
            count=count+1
        s=''.join([str(elem) for elem in s])
        print(s)
        return s
            
            
        
        
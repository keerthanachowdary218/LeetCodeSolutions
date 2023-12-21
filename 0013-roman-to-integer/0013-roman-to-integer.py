class Solution:
    def romanToInt(self, s: str) -> int:
        i=0
        result=0
        while i<=len(s)-1:
            if s[i]=='I':
                if (i+1)<len(s) and s[i+1]=='V':
                    result+=4
                    i=i+2
                    continue
                if (i+1)<len(s) and s[i+1]=='X':
                    result+=9
                    i=i+2
                    continue
                else:
                    result+=1
                    i=i+1
                    continue
            elif s[i]=='X':
                if (i+1)<len(s) and s[i+1]=='L':
                    result+=40
                    i=i+2
                    continue
                if (i+1)<len(s) and s[i+1]=='C':
                    result+=90
                    i=i+2
                    continue
                else:
                    result+=10
                    i=i+1
                    continue
            elif s[i]=='C':
                if (i+1)<len(s) and s[i+1]=='D':
                    result+=400
                    i=i+2
                    continue
                if (i+1)<len(s) and s[i+1]=='M':
                    result+=900
                    i=i+2
                    continue
                else:
                    result+=100
                    i=i+1
                    continue
            elif s[i]=='M':
                result+=1000
                i=i+1
                continue
            elif s[i]=='V':
                result+=5
                i=i+1
                continue
            elif s[i]=='L':
                result+=50
                i=i+1
                continue
            elif s[i]=='D':
                result+=500
                i=i+1
                continue
        return result
            
            
            
        
class Solution:
    def makeGood(self, s: str) -> str:
        #print(len(s))
        def IsGood(s):
            if s=="":
                return True
            if len(s)==1:
                return True
            if len(s)==2:
                if (s[0].islower() and s[1].isupper() and s[0]==s[1].lower()) or (s[1].islower() and s[0].isupper() and s[1]==s[0].lower()):
                    return False
            for i in range(0,len(s)-2):
                if (s[i].islower() and s[i+1].isupper() and s[i]==s[i+1].lower()) or (s[i+1].islower() and s[i].isupper() and s[i+1]==s[i].lower()):
                    return False
            return True
        if IsGood(s):
            return s
        else:
            while not IsGood(s):
                for i in range(0,len(s)-2):
                    #print(i,s)
                    if (s[i].islower() and s[i+1].isupper() and s[i]==s[i+1].lower()) or (s[i+1].islower() and s[i].isupper() and s[i+1]==s[i].lower()):
                        s = s[:i] + s[i + 2:]
                        break
                
                if len(s)>=2:
                    if (s[-2].islower() and s[-1].isupper() and s[-2]==s[-1].lower()) or (s[-1].islower() and s[-2].isupper() and s[-1]==s[-2].lower()):
                        s = s[:-1]
                        s = s[:-1]
                if len(s)==1:
                    return s
            return s
            
        
                    
        
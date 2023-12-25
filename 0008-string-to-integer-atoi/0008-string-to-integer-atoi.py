class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)>0:
            s=s.lstrip()
            i=0
            result=""
            print(s)
            neg=False
            if len(s)>0:
                if s[i]=="-":
                    neg=True
                    s = s[:i] + '' + s[i + 1:]
                    print(s)
                elif s[i]=="+":
                    s = s[:i] + '' + s[i + 1:]
                    print("replaced", s)
                elif s[i].isnumeric():
                    print(s)
                else:
                    return 0
                while i < len(s) and s[i].isdigit():
                        print(s[i])
                        result+=s[i]
                        print(result)
                        i+=1
                if result:
                        result = int(result)
                        print("here")
                        if neg:
                            result=result*(-1)
                        print(result)
                        if result<-2**31:
                            result = -2**31
                            return result
                        elif result>=2**31-1:
                            result=2**31-1
                            return result
                        else:
                            return result
            return 0
        return 0
            
            
        
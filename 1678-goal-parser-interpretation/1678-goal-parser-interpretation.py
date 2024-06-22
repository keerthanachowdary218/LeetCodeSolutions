class Solution:
    def interpret(self, command: str) -> str:
        res=''
        i=0
        while i<=(len(command)-1):
            if command[i]=='G':
                res+='G'
                i+=1
            elif command[i]=='(':
                if command[i+1]==')':
                    res+='o'
                    i=i+2
                else:
                    res+='al'
                    i+=4
            print(i)
        return res
            
                
        
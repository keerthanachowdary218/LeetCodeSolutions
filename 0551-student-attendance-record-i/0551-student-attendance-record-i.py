class Solution:
    def checkRecord(self, s: str) -> bool:
        count=0
        absent=0
        for i in s:
            if i=='L':
                count+=1
            elif i=='A':
                absent+=1
                count=0
            else:
                count=0
            if count==3:
                return False
            if absent>=2:
                return False
        return True
                
            
        
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        TotalCount=countL=countR=0
        for i in s:
            if i=='L':
                countL+=1
            else:
                countR+=1
            if countL==countR:
                TotalCount+=1
                countL=countR=0
        return TotalCount
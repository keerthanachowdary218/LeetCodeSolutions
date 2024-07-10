class Solution:
    def minOperations(self, logs: List[str]) -> int:
        print(logs)
        cur=0
        for i in logs:
            if i=='../':
                if cur!=0:
                    cur=cur-1
            elif i=='./':
                continue
            else:
                cur+=1
        return cur
                
                
                
        
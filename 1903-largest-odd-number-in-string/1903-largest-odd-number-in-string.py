class Solution:
    def largestOddNumber(self, num: str) -> str:
        h={"1","3","5","7","9"}
        ind=-1
        for i in range(len(num)-1,-1,-1):
            if num[i] not in h :continue
            ind=i
            break
        
        return num[:ind+1] if ind!=-1 else ""
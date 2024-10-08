class Solution:
    def minSwaps(self, s: str) -> int:
        #no.of unblanced open brackets(can be closed brackets as well)
        no_open=0
        for i in s:
            if i=='[':
                no_open+=1
            else:
                no_open-=1
            if no_open<0:
                no_open=0
        #print(no_open)
        return (no_open+1)//2
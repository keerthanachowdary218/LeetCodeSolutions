class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        binstart=bin(start)[2:][::-1]
        bingoal=bin(goal)[2:][::-1]
        #print(binstart,bingoal)
        if len(bingoal)<len(binstart):
            for i in range(len(binstart)-len(bingoal)):
                bingoal+='0'
        elif len(bingoal)>len(binstart):
            for i in range(len(bingoal)-len(binstart)):
                binstart+='0'
        #print(binstart,bingoal)
        count=0
        for i in range(0,len(binstart)):
            if binstart[i]!=bingoal[i]:
                count+=1
        return count
            
        
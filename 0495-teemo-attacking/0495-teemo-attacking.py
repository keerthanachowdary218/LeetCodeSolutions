class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        '''sett=set()
        for i in timeSeries:
            for j in range(i,i+duration):
                sett.add(j)
        return len(sett)
        '''
        res=0
        for i in range(0,len(timeSeries)-1):
            if timeSeries[i]+duration-1<timeSeries[i+1]:
                print(duration)
                res+=duration
            elif timeSeries[i]+duration-1>=timeSeries[i+1]:
                res+=timeSeries[i+1]-timeSeries[i]
        res+=duration
        return res
            
            
    
            
        
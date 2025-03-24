class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        print(meetings)
        #res=0
        res=meetings[0][0]-1 #starting meeting can be from day 2
        recent=meetings[0][1]
        for i in range(1,len(meetings)):
            start,end=meetings[i]
            if start>recent:
                res+=start-recent-1
            recent=max(recent,end)
        res+=days-recent
        return res

        
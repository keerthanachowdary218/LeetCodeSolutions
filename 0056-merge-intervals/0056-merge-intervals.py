class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        intervals.sort()
        print(intervals)
        prevstart,prevend=intervals[0]
        for start, end in intervals[1:]:
            if prevend >= start:
                prevend = max(prevend, end)
            else:
                res.append([prevstart, prevend])
                prevstart, prevend = start, end
        res.append([prevstart, prevend])
        return res


            
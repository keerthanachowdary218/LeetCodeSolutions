class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals
        intervals.sort()
        # initialize a list to return the merged intervals
        res=[intervals[0]]
        # from second element to the end of intervals
        for i in range(1,len(intervals)):
            # start,end = start and end of current interval
            start=intervals[i][0]
            end=intervals[i][1]
            # if end of current interval overlaps with the end of the last interval in the merged list
            if start<=res[-1][1]:
                # update the end of last interval in the merged list
                res[-1][1]=max(end,res[-1][1])
            else:
                # else add the current interval in the merged list
                res.append([start,end])
        return res      
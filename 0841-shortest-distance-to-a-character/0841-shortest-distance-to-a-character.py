class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        idx=len(s)
        res=[len(s)]*len(s)
        print(res)
        for i in range(len(s)):
            if s[i]==c:
                res[i]=0
                idx=0
            else:
                idx+=1
                res[i]=min(res[i],idx)
        print(res)
        for i in range(len(s)-1,-1,-1):
            if s[i]==c:
                res[i]=0
                idx=0
            else:
                idx+=1
                res[i]=min(res[i],idx)
        return res
        for i in range(len(s)-2,-1,-1):
            res[i]=min(res[i+1]+1,res[i])
        return res
        '''
        shortest_dist = []
        size = len(s)
        if size == 1:
            return [0]
        for idx, char in enumerate(s):
            if char == c:
                shortest_dist.append(0)
            else:
                if idx == 0:
                    shortest_dist.append(size)
                else:
                    shortest_dist.append( shortest_dist[-1] + 1)            
        for idx in range(2, size+1):
            shortest_dist[-idx] = min(shortest_dist[-idx], shortest_dist[-idx+1]+1 ) 
        return shortest_dist
        '''
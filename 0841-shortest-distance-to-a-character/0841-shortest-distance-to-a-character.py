class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
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
        
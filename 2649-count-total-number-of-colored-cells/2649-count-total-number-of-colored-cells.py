class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=1
        for i in range(2, n+1):    
            sum+=(i-1)*4
        return sum  
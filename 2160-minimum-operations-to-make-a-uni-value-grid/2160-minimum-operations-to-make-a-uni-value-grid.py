class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        gridarr=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                gridarr.append(grid[i][j])
        print(gridarr)
        gridarr.sort()
        mid=gridarr[(len(gridarr)//2)]
        res = 0
        for i in gridarr:
            if abs(i - mid) % x != 0:
                return -1
            res += abs(i - mid) // x
        return res


        
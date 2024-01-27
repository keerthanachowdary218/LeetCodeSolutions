class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        result=self.climbStairs(n-1)+self.climbStairs(n-2)
        print(result)
        return result
    '''
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        return self.solve(n, dp)

    def solve(self, n, dp):
        if dp[n] != -1:
            return dp[n]

        dp[n] = self.solve(n - 1, dp) + self.solve(n - 2, dp)

        return dp[n]

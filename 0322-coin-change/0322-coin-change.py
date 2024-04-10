class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp=[float(inf)]*(amount+1)
        dp[0]=0
        for i in coins:
            if i <= amount:
                dp[i]=1
        for i in range(amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i]=min(dp[i],1+dp[i-j])
        print(dp[-1],dp)
        if dp[-1]==float(inf):
            return -1
        else:
            return dp[amount]
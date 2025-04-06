class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=float('-inf')
        curmin=prices[0]
        for i in prices:
            curmin=min(curmin,i)
            profit=max(profit,i-curmin)
        return profit
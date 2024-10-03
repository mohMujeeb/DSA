class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        maxprofit = 0
        mini = prices[0]

        for i in range(n):
            cost = prices[i] - mini
            maxprofit = max(maxprofit, cost)
            mini = min(mini, prices[i])

        return maxprofit
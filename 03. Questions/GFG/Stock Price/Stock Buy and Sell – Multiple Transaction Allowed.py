"""
The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock 
i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.
Note: Buying and selling the stock can be done multiple times, but you can only hold one stock at a time. In order 
to buy another stock, firstly you have to sell the current holding stock.

Examples:

Input: prices[] = [3, 4, 1, 5]
Output: 5
Explanation: We can buy stock on day 1 (at price 3) and sell it on day 2 (at price 4) profit will be 4 - 3 = 1, 
We can buy another stock on day 3 (at price 1) and sell it on day 4 (at price 5) profit will be 5 - 1 = 4, 
which will give us maximum profit of 1 + 4 = 5.
"""

def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

prices = [3, 4, 1, 5]
print(max_profit(prices))  # Output: 5
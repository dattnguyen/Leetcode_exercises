# Say you have an array prices for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

def maxProfit(prices):
    min_day = prices[0]
    max_profit = 0

    for i in prices:
        min_day = min (min_day,i) #determine if today stock goes up or down
        profit = i - min_day #calculate the profit

        if profit > 0: #if we have profit, we increase the max_profit
            max_profit += profit
            min_day = i #and reset the min_day to the current iterable value

    return print(max_profit)

maxProfit([7,1,5,3,6,4])
#%%
def maxProfit2(prices):
    if not prices or len(prices) == 1: #corner case
        return 0
    max_profit = 0

    for i in range (1, len(prices)):
        if prices[i] > prices[i-1]: # if today's price is greater than yesterday's price, we sell the stock
            max_profit += prices[i]-prices[i-1]

    return print(max_profit)

maxProfit2([7,9,2,3,5,1,9])
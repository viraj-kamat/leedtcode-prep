# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


def computeProfit(prices):

    length = len(prices)

    if prices == None or length == 0:
        return 0

    minVal = prices[0]
    profit = 0

    for i in range(1,length):
        profit = max(profit, prices[i]-minVal)
        minVal = min(minVal, prices[i])


    return profit


assert computeProfit([7, 1, 5, 3, 6, 4]) == 5
assert computeProfit([7, 6, 4, 3, 1]) == 0
assert computeProfit([1, 2]) == 1
assert computeProfit([2, 1]) == 0
assert computeProfit([2, 4, 1]) == 2
assert computeProfit([3, 2, 6, 5, 0, 3]) == 4
assert computeProfit([1]) == 0
assert computeProfit([]) == 0
print("all tests passed")

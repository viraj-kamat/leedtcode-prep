# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# https://www.youtube.com/watch?v=1pkOgXD63yU



def maxProfit(prices):

    if len(prices) == 0 :
        return 0
    minSoFar = float("inf")
    profit = 0

    for p in prices:
        if minSoFar == float("inf"):
            minSoFar = p
            continue
        profit = max(profit, p-minSoFar)
        minSoFar = min(minSoFar, p)
    return profit


assert maxProfit([7,1,5,3,6,4]) == 5
assert maxProfit([7,6,4,3,1]) == 0
assert maxProfit([]) == 0
assert maxProfit([5]) == 0
assert maxProfit([2,4,1]) == 2
assert maxProfit([1,2,3,4,5]) == 4
assert maxProfit([3,3,3,3]) == 0
print("All tests passed")

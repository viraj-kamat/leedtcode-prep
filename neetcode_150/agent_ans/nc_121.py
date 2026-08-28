# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def maxProfit(prices):
    min_price = float("inf")
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best

from typing import List


def maxProfit(prices: List[int]) -> int:

    if len(prices) == 1:
        return 0

    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        profit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1

    return max_profit


if __name__ == "__main__":
    prices = [7, 6, 4, 3, 1]
    maxProfit(prices)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        totalprofit=0
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            totalprofit+=profit
            min_price = prices[i]
        return totalprofit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        dp = [0] * len(prices)
        
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            if profit > 0:
                dp[i] = profit
                min_price = prices[i]
            
        return sum(dp)
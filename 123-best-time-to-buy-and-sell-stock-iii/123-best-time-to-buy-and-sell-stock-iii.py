class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return []
        maxprofit=0
        profit=[]
        currmin=prices[0]
        for price in prices:
            currmin=min(currmin,price)
            maxprofit=max(maxprofit,price-currmin)
            profit.append(maxprofit)
        totalprofit=0
        maxprofit=0
        currmax=prices[-1]
        for i in range(len(prices)-1,-1,-1):
            currmax=max(currmax,prices[i])
            maxprofit=max(maxprofit,currmax-prices[i])
            totalprofit=max(totalprofit,maxprofit+profit[i])
        return totalprofit
       
      
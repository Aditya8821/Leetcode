class Solution:
    def countOrders(self, n: int) -> int:
        if n==1: return 1 
        dp=[1]*n
        
        for i in range(1,len(dp)):
            x=(i*2)+1
            dp[i]=dp[i-1]*(x*(x+1)//2)
        print(dp)
        return dp[-1]%(10**9+7)
            
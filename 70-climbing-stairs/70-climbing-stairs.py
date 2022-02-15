class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        dp=[0]*(n+1)
        dp[1],dp[2]=1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        
        
        
        # a,b=1,1
        # for _ in range(n):
        #     a,b=b,a+b
        # return a
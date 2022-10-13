class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            l=0
            r=i-1
            while l<=n-1:
                dp[i]+=dp[l]*dp[r]
                l+=1
                r-=1
        return dp[n]
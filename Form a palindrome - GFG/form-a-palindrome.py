#User function Template for python3

class Solution:
    def findMinInsertions(self, s):
        # code here
        n = len(s)
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for g in range(n):
            for i,j in zip(range(n-g),range(g,n)):
                if g == 0 :
                    dp[i][j] = 0
                elif g == 1:
                    if s[i] != s[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = 1+ min(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.findMinInsertions(S))
# } Driver Code Ends
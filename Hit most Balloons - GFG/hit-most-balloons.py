#User function Template for python3

class Solution: 
    def mostBalloons(self, N, arr):
        # Code here
        ans=1
        for i in range(N):
            count=dict()
            samepos=0
            for j in range(N):
                xdiff=arr[j][0]-arr[i][0]
                ydiff=arr[j][1]-arr[i][1]
                if xdiff==0 and ydiff==0:
                    samepos+=1
                else:
                    slope=float("inf") if ydiff==0 else xdiff/ydiff
                    count[slope]=count.get(slope,0)+1
            ans=max(ans,max(count.values())+samepos)
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input()) 
        arr=[[] for j in range(N)]
        for j in range(2): 
            inp = [int(i) for i in input().split()] 
            for i in range(N): 
                arr[i].append(inp[i])
        ob = Solution()
        print(ob.mostBalloons(N, arr))
        
        T -= 1
# } Driver Code Ends
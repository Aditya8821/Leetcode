class Solution:
    def findSum(self,A,N): 
        #code here
        maxi=-1000000000
        mini=1000000000
        for i in A:
            if i>maxi: maxi=i
            if i<mini: mini=i
        return maxi+mini



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends
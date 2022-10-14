#User function Template for python3

class Solution:
    
    def maximizeSum (self,arr, n) : 
        #Complete the function
        d={}
        for i in range(n):
            if arr[i] in d:
                d[arr[i]]+=1
            else:
                d[arr[i]]=1
        res=0
        i=max(arr)
        while i>0:
            if i in d and d[i]>0:
                res+=i
                if i-1 in d:
                    d[i-1]-=1
                d[i]-=1
            else:
                i-=1
        return res
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ob=Solution()
    
    ans = ob.maximizeSum(arr, n)
    print(ans)

    





# } Driver Code Ends
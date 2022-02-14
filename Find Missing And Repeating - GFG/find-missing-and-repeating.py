#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n):
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=[]
        for i in range(1,n+1):
            if i in d and d[i]==2:
                res.append(i)
                break
        for i in range(1,n+1):
            if i not in d:
                res.append(i)
                break
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
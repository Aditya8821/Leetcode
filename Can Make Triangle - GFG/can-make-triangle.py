#User function Template for python3
class Solution:
    def canMakeTriangle(self, A, N): 
        #code here
        start,end=0,2
        res=[]
        while end<=N-1:
            if A[start]+A[start+1]<=A[end] or A[end]+A[start+1]<=A[start] or A[start]+A[end]<=A[start+1]:
                res.append(0)
            else:
                res.append(1)
            start+=1
            end+=1
        return res


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.canMakeTriangle(A, N)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
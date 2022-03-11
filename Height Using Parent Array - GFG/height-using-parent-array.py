#User function Template for python3

class Solution:
    def findHeight(self, N, arr):
        # code here
        arr[0] = 1 
        for i in range(1,N):
            arr[i] = arr[arr[i]] + 1
        return arr[N-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.findHeight(N, arr))
# } Driver Code Ends
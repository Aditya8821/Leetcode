#User function Template for python3

class Solution:
    def newIPAdd(self, S):
        # code here
        return ".".join(str(int(i)) for i in S.split("."))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.newIPAdd(s)
        print(ans)
# } Driver Code Ends
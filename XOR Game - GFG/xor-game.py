#User function Template for python3

class Solution:
    def xorCal(self, k):
        # code here
        if k == 1:
            return 2
        if k == 3:
            return 1
        if k == 7:
            return 3
        if k == 15:
            return 7
        if k == 31:
            return 15
        if k == 63:
            return 31
        return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())
        
        ob = Solution()
        print(ob.xorCal(k))
# } Driver Code Ends
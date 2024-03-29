#User function Template for python3
class Solution:
    def countStrings(self, S): 
        #code here
        n = len(S)
        charSet = {}
        count = 0
        for i in S:
            if i in charSet:
                count = count + charSet[i] + 1
                charSet[i] += 1
            else:
                charSet[i] = 0
        ans = (n*(n-1)) // 2
        if(count >0):
            ans = ans - count + 1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countStrings(S)
        print(ans)
# } Driver Code Ends
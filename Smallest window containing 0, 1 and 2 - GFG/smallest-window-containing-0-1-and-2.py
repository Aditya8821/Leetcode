#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        ans=[-1,-1,-1]
        mini=(1<<31)
        if not S.count("0") or not S.count("1") or not S.count("2"): return -1
        for idx,val in enumerate(S):
            ans[int(val)]=idx
            if -1 not in ans:
                mini=min(mini,max(ans)-min(ans)+1)
        return mini

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends
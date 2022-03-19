#User function Template for python3

class Solution:
	def findRank(self, S):
		#Code here
		def fact(n):
            f=1
            while n>=1:
                f*=n
                n-=1
            return f
        
        def findSmallerinRight(st,low,high):
            c,i=0,low+1
            while i<=high:
                if(st[i]<st[low]):
                    c+=1
                i+=1
            return c
        l=len(S)
        mul=fact(l)
        rank=1
        i=0
        
        while i<l:
            mul//=(l-i)
            countRight=findSmallerinRight(S,i,l-1)
            rank+=(countRight*mul)
            i+=1
        return rank

#{ 
#  Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	str = input().strip()
    	obj = Solution()
    	ans = obj.findRank(str)
    	print(ans)
# } Driver Code Ends
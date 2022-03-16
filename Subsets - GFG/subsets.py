#User function Template for python3
from itertools import combinations
class Solution:
    def subsets(self, A):
        ans=[()]
        for x in range(1,len(A)+1):
            l=list(combinations(A,x))
            for i in l:
               ans.append(i)
        return sorted(ans)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here 
        c = 1
        sc = 0;
        s = A
        for i in range(int(len(B)/len(A))+1):
            x = s.count(B)
            if x>0:
               
                sc = sc+1
                break
           
            c = c+1
            s = s+A
        if sc>0:
            return c
        else:
            return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends
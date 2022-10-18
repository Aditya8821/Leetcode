#User function Template for python3

def downwardDigonal(N, A): 
    # code here
    ans=[]
    for i in range(2*N-1):
        for j in range(N):
            if i-j<0:
                break
            elif i-j<N:
                ans.append(A[j][i-j])
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
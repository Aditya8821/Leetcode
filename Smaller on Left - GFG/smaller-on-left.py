#User function Template for python3

import bisect
def Smallestonleft (arr,  n) : 
    #Complete the function
    stack = []
    ans = []
    ans.append( -1)
    stack.append(arr[0])
    for i in range(1,n):
        bisect.insort(stack,arr[i])
        it = bisect.bisect_left(stack,arr[i])
        #print(it,arr[i])
        #print(stack)
        if (it):
            #print(stack[it-1],arr[i])
            ans.append(stack[it-1])
        else:
            ans.append(-1)
    return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = Smallestonleft(arr, n);
    for each in res:
        print(each,end=' ')
    print()




# } Driver Code Ends
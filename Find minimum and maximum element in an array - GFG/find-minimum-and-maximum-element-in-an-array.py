#User function Template for python3

def getMinMax( a, n):
    mini,maxi=0,0
    if n==1:
        return [a[0],a[0]]
    if a[0]>a[1]:
        mini=a[1]
        maxi=a[0]
    else:
        mini=a[0]
        maxi=a[1]
    for i in range(2,n):
        if a[i]>maxi:
            maxi=a[i]
        elif a[i]<mini:
            mini=a[i]
    return [mini,maxi]
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends
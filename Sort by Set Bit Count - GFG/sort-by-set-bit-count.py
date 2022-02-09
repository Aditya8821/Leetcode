#User function Template for python3

class Solution:
    def func(self, n):
       return bin(n).count('1')
    def sortBySetBitCount(self, arr, n):
        arr.sort(key=self.func,reverse=True)
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends
from typing import List
# class Solution:
    # def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
        # code here
class tree:

    def __init__(self,data):

        self.data=data

        self.left=self.right=None

class Solution:

    def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:

        def insert(val,root,succ):

            #print(succ,root,val)

            if not root:

                return tree(val),succ

                

            #print(succ,root.data,val)    

            if root.data>val:

                succ=root

                node,succ=insert(val,root.left,succ)

                root.left=node

            else:

                node,succ=insert(val,root.right,succ)

                root.right=node

               

            return root,succ

        ans=[-1]*n

        head=None

        for i in range(n-1,-1,-1):

            head,succ=insert(arr[i],head,None)

            if succ:

                ans[i]=succ.data

        return ans
                



#{ 
 # Driver Code Starts


class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findLeastGreater(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends
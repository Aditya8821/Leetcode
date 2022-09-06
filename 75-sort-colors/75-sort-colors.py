class Solution:
    # This probelm is also known as Dutch Flag Problem
    def sortColors(self, arr: List[int]) -> None:
        #n=len(arr)
        # c0,c1,c2=0,0,0
        # for i in range(n):
        #     if arr[i]==0: c0+=1
        #     elif arr[i]==1: c1+=1
        #     else: c2+=1
        # for i in range(c0):
        #     arr[i]=0
        # for i in range(c0,c0+c1):
        #     arr[i]=1
        # for i in range(c0+c1,n):
        #     arr[i]=2
        # return arr
        
    
        # low=0
        # pointer=0
        # high=n-1
        # while(pointer<=high):
        #     if arr[pointer]==0:
        #         arr[low],arr[pointer]=arr[pointer],arr[low]
        #         pointer+=1
        #         low+=1
        #     elif arr[pointer]==1:
        #         pointer+=1
        #     else:
        #         arr[pointer],arr[high]=arr[high],arr[pointer]
        #         high-=1
        # return arr
        
        n=len(arr)
        n0,n1,n2=0,0,0
        for x in arr:
            if x==0:
                arr[n2]=2
                n2+=1
                arr[n1]=1
                n1+=1
                arr[n0]=0
                n0+=1
            elif x==1:
                arr[n2]=2
                n2+=1
                arr[n1]=1
                n1+=1
            else:
                arr[n2]=2
                n2+=1
        return arr
        
class Solution:
    def canReach(self, arr: List[int], i: int) -> bool:
        if i<0 or i >=len(arr) or arr[i]<0: return False
        arr[i]*=-1
        return arr[i]==0 or self.canReach(arr,i-arr[i]) or self.canReach(arr,i+arr[i]) 
       

        
        
        # if arr[start]==0: return True
        # zero_index=0
        # for i in range(len(arr)):
        #     if arr[i]==0: 
        #         zero_index=i
        # n=len(arr)
        # def solve(ind):
        #     if ind==start: return False
        #     if ind==zero_index: return True
        #     if ind>=n or ind<0: return False
        #     elif ind>zero_index:
        #         return solve(ind-arr[ind])
        #     else:
        #         return solve(ind+arr[ind])
        # return (solve(start+arr[start]) or solve(start-arr[start]))
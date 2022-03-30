class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final=[]
        def solve(index,candidates,tar,final,res):
            if index==len(candidates):
                if tar==0:
                    final.append(res.copy())
                    return
                return 
            if candidates[index]<=tar:
                res.append(candidates[index])
                solve(index,candidates,tar-candidates[index],final,res)
                res.pop()
            solve(index+1,candidates,tar,final,res)
        solve(0,candidates,target,final,[])
        return final
            
        
        
        
        
        
        # ans=[]
        # def solve(candidates,tar,res,idx):
        #     if tar==0:
        #         ans.append(res[:])
        #         return
        #     if tar<0:
        #         return
        #     for index in range(idx,len(candidates)):
        #         res.append(candidates[index])
        #         solve(candidates,tar-candidates[index],res,index)
        #         res.pop()
        # solve(candidates,target,[],0)
        # return ans